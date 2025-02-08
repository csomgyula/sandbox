from numpy import exp
from math import sin, cos, pi, sqrt

"""
Logistic function - one variable case

https://en.wikipedia.org/wiki/Logistic_function
"""

def logistic(x):
    """    
    https://en.wikipedia.org/wiki/Logistic_function
    """
    return 1 / (1 + exp(-x))
    
def logistic_derivate(x):
    """
    https://en.wikipedia.org/wiki/Logistic_function#Derivative
    """
    func = logistic(x)
    return func * (1-func)
      
class GradientDescent:
    def __init__(self, function_name, function, method_name, adjust_calc, max_iteration = 100, min_squared_error = 0.01, initial_value = 100):
        self.method_name = method_name
        self.function_name = function_name
        self.function = function
        self.adjust_calc = adjust_calc
        self.initial_value = initial_value
        self.max_iteration = max_iteration
        self.min_squared_error = min_squared_error  
        
    def __call__(self, function_value):
        print(f"Gradient Descent by {self.method_name} search for {self.function_name}={function_value} started")
        print(f"max iteration: {self.max_iteration}, min squared error: {self.min_squared_error}, initial value: {self.initial_value}")
        
        val = self.initial_value
        for i in range(self.max_iteration):
           func_val = self.function(val)
           
           error = func_val - function_value
           squared_error = error * error
           #print(f"se: {squared_error}, min se: {self.min_squared_error}, {squared_error < self.min_squared_error}")
           if squared_error < self.min_squared_error:
               break
               
           adjust = self.adjust_calc(val, func_val, error)
           val -= adjust
               
           print(f"{i+1}: val: {val}, func_val: {func_val}, squared_err: {squared_error}, adjust: {adjust}")
           
        print(f"{self.method_name} search for {self.function_name}={function_value} finished")
        print(f"val: {val}, func_val: {func_val}, squared err: {squared_error}, iterations: {i+1}\n")    
        
        return val, func_val, squared_error

class GradientDescentByDifferentialQuotient(GradientDescent):
    def __init__(self, function_name, function):
        adjust_calc = lambda val, func_val, error: 2 * error * self.differential_quotient(val)
        
        super().__init__(function_name, function, "differential quotient", adjust_calc)

    def differential_quotient(self, x, delta_x = 0.01, func_diff_min = 0.01, func_diff_max = 1, max_iteration = 100):
        function = self.function
        
        func_x = function(x)
        iteration = 0
        
        """
        main loop to find delta
        """
        while(True): 
            iteration += 1
            func_x_p_dx  = function(x + delta_x)
            func_x_m_dx = function(x - delta_x)
            #print(f"debug-function_differential: iter: {iteration}, delta: {delta_x}, func_plus: {func_plus}, func_minus: {func_minus}")
            
            if iteration > max_iteration:
                break
            
            # too small
            if abs(func_x_p_dx - func_x) < func_diff_min and abs(func_x - func_x_m_dx) < func_diff_min: 
                delta_x *= 2
            # too big
            elif abs(func_x_p_dx - func_x) > func_diff_max and abs(func_x - func_x_m_dx) > func_diff_max:
                delta_x *= 0.5
            else:
                break
                
        diff_quot_plus  = (func_x_p_dx - func_x) / delta_x
        diff_quot_minus = (func_x - func_x_m_dx) / delta_x
            
        if diff_quot_minus >= 0 and diff_quot_plus >= 0:
            diff_quot = max(diff_quot_minus, diff_quot_plus)
        elif (diff_quot_minus <= 0 and diff_quot_plus <= 0):
            diff_quot = min(diff_quot_minus, diff_quot_plus)
        else:
            diff_quot = 0
        #print(f"debug-function_diff_quot result: {diff_quot}, iterations: {iteration}")
        return diff_quot

class LogisticGradientDescentByDerivate(GradientDescent):
    def __init__(self):
        function_name = "Logistic"
        function = logistic
        adjust_calc = lambda val, func_val, error: 2 * error * logistic_derivate(val)
        
        super().__init__(function_name, function, "derivate", adjust_calc)
        
class LogisticGradientDescentByDifferentialQuotient(GradientDescentByDifferentialQuotient):
    def __init__(self):
        function_name = "Logistic"
        function = logistic
        
        super().__init__(function_name, function)

class ScaledNeuralGradientDescent:
    """
    Learnt from the raw experiments (GradientDescent) neither derivate, nor differential quotient works
    on the platou (for large values where derivate is nearly zero). Instead 
    
    1. We use a discrete approach, instead of differential we simply adjust by searching for a logistic argument 
       in the form of (weight * initial_value, bias) where the logistic value is closer to the given. 
       In that regard:
    2. The approach is similar to the LogisticGradientDescentByDifferentialQuotient, since that 
       is also a discrete approach. However: 
    3. We still use the derivate though, not its value but its gradient direction. We do not calculate the derivate
       value (which can be close to zero), instead the gradient direction, which is known to be: 
       
       (value, 1)
    
       since the derivate by weight is value times more than the derivate by bias.
       
    4. The speed of gradient descent is dynamically scaled   
    """   
    
    def __init__(self, function_name, function, max_argument_iteration = 100, max_delta_iteration = 1000, min_error = 0.001, input_value = 1000, delta = 0.001, delta_scale = 2):
        self.function_name = function_name
        self.function = function
        self.max_argument_iteration = max_argument_iteration
        self.max_delta_iteration = max_delta_iteration
        self.min_error = min_error      
        self.input_value = input_value
        self.delta = delta
        self.delta_scale = delta_scale
        self.initial_weight = 1
        self.initial_bias = 0
    
    def __call__(self, function_value):
        print(f"Neural Gradient Descent search for {self.function_name}={function_value} started")
        print(f"max arg iteration: {self.max_argument_iteration}, max delta iteration: {self.max_delta_iteration}, min error: {self.min_error}, input: {self.input_value}")
        print()
        
        #print(f"\tinit")
        input_val  = self.input_value
        min_err    = self.min_error
        
        weight, bias, func_arg, func_arg_val, error = self.init_func_arg_val_error(self.initial_weight, input_val, self.initial_bias, function_value)
        delta_iterations = 0
        
        #print(f"\tmain loop")
        for i in range(self.max_argument_iteration):
            print(f"\niter-{i+1}: weight: {weight}, input: {input_val}, bias: {bias}, arg: {func_arg}, func arg val: {func_arg_val}, err: {error}, delta: {self.delta}, delta iterations: {delta_iterations}")
            
            if error < min_err:
               break

            weight, bias, func_arg, func_arg_val, error, delta_iterations = self.adjust_weight_and_bias(weight, input_val, bias, function_value, error)

        print(f"\nNeural Gradient Descent search for {self.function_name}={function_value} finished")
        print(f"weight: {weight}, input: {input_val}, bias: {bias}, arg: {func_arg}, func arg val: {func_arg_val}, err: {error}")

    def adjust_weight_and_bias(self, weight, input_value, bias, function_value, error):
        #print(f"\trun adjust_weight_and_bias")
        function = self.function
        min_err    = self.min_error
        grad_weight, grad_bias = self.gradient(input_value)
        adj_weight, adj_bias, adj_func_arg, adj_func_arg_val, adj_error = None, None, None, None, None
        delta_iterations = 0
        """
        main loop to find delta and adjustment according to it
        """
        for delta in self.deltas():
            if not(delta):
                break
            
            delta_iterations += 1
            #print(f"\tdelta: {delta}")
            pos_weight, pos_bias, pos_func_arg, pos_func_arg_val, pos_error = self.candidate_adjustment(weight, input_value, bias, function_value, delta,  grad_weight, grad_bias)
            neg_weight, neg_bias, neg_func_arg, neg_func_arg_val, neg_error = self.candidate_adjustment(weight, input_value, bias, function_value, -delta, grad_weight, grad_bias)

            if pos_error < neg_error:
                #print("\tpositive grad direction")
                cand_weight, cand_bias, cand_func_arg, cand_func_arg_val, cand_error = pos_weight, pos_bias, pos_func_arg, pos_func_arg_val, pos_error
            else: 
                #print("\tnegative grad direction")
                cand_weight, cand_bias, cand_func_arg, cand_func_arg_val, cand_error = neg_weight, neg_bias, neg_func_arg, neg_func_arg_val, neg_error

            debug = f"\tcand_weight: {cand_weight}:, cand_bias: {cand_bias}, cand_func_arg: {cand_func_arg}, cand_func_arg_val: {cand_func_arg_val}, cand_error: {cand_error} < error: {error}? {cand_error < error}, delta: {delta}"
            if cand_error < error and (not(adj_error) or cand_error < adj_error):  
                #print(f"\t***** candidate is better:\n\t{debug}\n")                
                adj_weight, adj_bias, adj_func_arg, adj_func_arg_val, adj_error = cand_weight, cand_bias, cand_func_arg, cand_func_arg_val, cand_error
                self.delta = delta
                if cand_error < min_err or cand_error < error / 2:
                    break
            else:
                #print(f"\t     candidate is not better:\n\t{debug}\n")
                pass
                
        return adj_weight, adj_bias, adj_func_arg, adj_func_arg_val, adj_error, delta_iterations
    
    def init_func_arg_val_error(self, weight, input_value, bias, function_value):
        #print(f"\trun init_func_arg_val_error")
        return self.candidate_adjustment(self.initial_weight, input_value, self.initial_bias, function_value)
        
    def candidate_adjustment(self, weight, input_value, bias, function_value, delta=0, grad_weight=0, grad_bias=0):
        if abs(delta) > 0:
            weight       = weight + grad_weight * delta
            bias         = bias + grad_bias * delta
        func_arg     = weight * input_value + bias
        func_arg_val = self.function(func_arg)
        error        = abs(func_arg_val - function_value)
        
        return weight, bias, func_arg, func_arg_val, error
    
    def gradient(self,input_val):
        """
        Returns the gradient (direction) as a one length vector in which the function increases most
        """
        #print(f"\trun gradient")
        input_val_1_length = sqrt(input_val^2 + 1)
        return input_val / input_val_1_length, 1 / input_val_1_length
        
    def deltas(self):
        delta = self.delta
        delta_scale = self.delta_scale
        min_delta = delta / 2
        max_delta = delta * 2
        
        for iteration in range(self.max_delta_iteration):
            if iteration == 0:
                delta = self.delta
            elif iteration % 2 == 0:
                delta = min_delta
                min_delta /= delta_scale
            else:
                delta = max_delta
                max_delta *= delta_scale
            yield delta
        yield None
        
class ScaledNeuralLogisticGradientDescent(ScaledNeuralGradientDescent):
    def __init__(self, input_value = 1000):
        function_name = "Logistic"
        function = logistic
        super().__init__(function_name, function, input_value = input_value)
    
if __name__ == "__main__":       
    #LogisticGradientDescentByDerivate()(function_value = 0.5)
    #LogisticGradientDescentByDifferentialQuotient()(function_value = 0.5)
    ScaledNeuralLogisticGradientDescent(input_value = 512)(function_value = 0.5)
    iv = 1
    for i in range(16):
        iv *= 2
        
        try:
            #ScaledNeuralLogisticGradientDescent(input_value = iv)(function_value = 0.5)
            pass
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            
        print()