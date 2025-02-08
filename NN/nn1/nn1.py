from numpy import exp, array, random, dot, sum

class Set:
    def __str__(self):
        str = ""
        for i in range(self.inputs.size):
            str += f"{self.inputs[i]} -> {self.outputs[i]}\n"
        return str    

class TrainingSet(Set):
     def __init__(self):
         self.inputs  = array([-3, -2, -1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 10])
         self.outputs = array([1,   1,  1, 1, 1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 0, 0, 0])
         
class SampleSet(Set):
     def __init__(self):
         self.inputs  = array([-100, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 100])
         self.outputs = None
         
class NeuralNet:
    def __init__(self):
        self.weight = Random().integer(-1,1)
        self.bias   = Random().integer(-1,1)
        self.activation = Logistic()
        self.rate = 10
        
    def configure(self, inputs, expected_outputs, iterations):
        for iteration in range(iterations):
            # calculate outputs
            calculated_outputs = self.outputs(inputs)
            
            # calculate errors
            errors  = calculated_outputs - expected_outputs
            mse = dot(errors, errors) / inputs.size
            print(f"{iteration}: weight: {self.weight}, bias: {self.bias}, MSE: {mse}")
            
            # adjust weights and bias
            (d_weight, d_bias) = self.adjustment(inputs, errors)
            self.weight += d_weight
            self.bias += d_bias
            
    def outputs(self, inputs):
        return self.activation.function(inputs, self.weight, self.bias)
        
    def adjustment(self, inputs, errors):
        derivates_by_weight  = self.activation.derivative_by_weight(inputs, self.weight, self.bias)
        derivates_by_bias    = self.activation.derivative_by_bias(inputs, self.weight, self.bias)
        error_weight_gradients = 2 * dot(errors, derivates_by_weight)
        error_bias_gradients   = 2 * dot(errors, derivates_by_bias)
        return (self.rate * sum(error_weight_gradients)/inputs.size, self.rate * sum(error_bias_gradients)/inputs.size)
        
class Logistic:
    def function(self, value, weight, bias):
        """
        Logistic function in one dimensional case 
        https://en.wikipedia.org/wiki/Logistic_function
        """
        return 1 / (1 + exp(weight * value + bias))
         
    def derivative_by_weight(self, value, weight, bias):
        """
        Derivate logistic function by weight
        https://en.wikipedia.org/wiki/Logistic_function#Derivative
        """
        log = self.function(value, weight, bias)
        return value * log * (1-log)
        
    def derivative_by_bias(self, value, weight, bias):
        """
        Derivate logistic function by bias
        https://en.wikipedia.org/wiki/Logistic_function#Derivative
        """
        log = self.function(value, weight, bias)
        return log * (1-log)

class Random:
     def __init__(self):
         self.generator = random.default_rng(87807082188168775992250206045920274312)
         # https://numpy.org/doc/stable/reference/random/generator.html
         
     def integer(self, low, high):
        return self.generator.integers(low, high, endpoint=True)
        
if __name__ == "__main__":
    nn = NeuralNet()
    
    training_set = TrainingSet()    
    print(training_set)
    
    nn.configure(training_set.inputs, training_set.outputs, 50000)
    
    sample_set = SampleSet()
    sample_set.outputs = nn.outputs(sample_set.inputs)
    
    print(sample_set)
    