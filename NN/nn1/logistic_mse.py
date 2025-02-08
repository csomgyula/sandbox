from numpy import exp, array, random, dot, sum, meshgrid, linspace
import matplotlib.pyplot as plt

class LogisticMSE:
    """
    Concept:

    1. generate NN1 samples (r, 0|1), r in R
       - now: modal, multimodal Gaussian distrib
    2. calculate NN1 approximations and MSE errors for multiple weights and biases
       - bias within cca. the sample span (no need to diverge from it, but I would still like to see the borders)
       - weight donno, now I do not see much value in it
    3. plot the 2D (weight, bias) diagram, display or save as image
    
    Design:
    - use simple design
    - is a method (or process) object
    - is not thread safe, one object one run in parallel
    """    
    def __init__(self):
        print("PROC PROTO:\tNN1 error diagram prototype object creation started")
        self.samples = []
        self.weights = None
        self.biases = None
        self.mses = None
        print("PROC PROTO:\tNN1 error diagram prototype object  creation finished")
        
    def __call__(self):
        print("PROC PROTO:\tNN1 error diagram generation started")
        self.generate_samples()
        self.calculate()
        self.plot()
        print("PROC PROTO:\tNN1 error diagram generation finished")
        
    def generate_samples(self):
        """
        - generate NN1 samples (r, 0|1), r in R
        - now: modal, multimodal Gaussian distrib
        """
        print("PROC PROTO:\tGenerate NN1 samples")
        
        # now deterministic then add rnd        
        samples = self.samples
        samples.append([-100, 0])     
        samples.append([-50, 0])     
        samples.append([-20, 0])  
        samples.append([-10, 0])
        samples.append([-5, 0])
        samples.append([-2, 0])
        samples.append([-1, 0])    
        samples.append([100, 1])     
        samples.append([50, 1])     
        samples.append([20, 1])  
        samples.append([10, 1])
        samples.append([5, 1])
        samples.append([2, 1])
        samples.append([1, 1])
        print(f"sample size: {len(samples)}")
        print(f"samples:\n{array(samples)}")
        
    class Calc:
        """
        Concept:
        - calculate NN1 approximations and MSE errors for multiple weights and biases
        - bias within cca. the sample span (no need to diverge from it, but I would still like to see the borders)
        - weight donno, now I do not see much value in it
        
        Design:
        - for simplicity use a numpy meshgrid structure easy for ploting:
        - weights are X-s of meshgrid
        - biases are Y-s of meshgrid
        - mses are Z-s of meshgrid
        - each is 2D array
        - see:
        - https://matplotlib.org/stable/plot_types/3D/wire3d_simple.html
        - https://numpy.org/doc/2.1/reference/generated/numpy.meshgrid.html
        - https://numpy.org/doc/2.1/reference/generated/numpy.linspace.html
        """
        def __init__(self, samples, step = 1):
            print("PROC CALC:\tCalc object creation started")
            self.samples = array(samples)
            self.step = step
            self.weights = None
            self.biases = None
            self.mses = None
            print("PROC CALC:\tCalc object creation finished")
            
        def __call__(self):
            self.space()
            self.approximations_and_mses()
    
        def space(self):
            print("PROC CALC:\tCalculate weight and bias space started")
            
            self.weight_space = linspace(-10, 10, 21, endpoint = True)
            bs_min, bs_max = self.sample_span() # min, max
            self.bias_space =  linspace(bs_min, bs_max, 1 + int(bs_max - bs_min / self.step), endpoint = True)
            
            self.weights, self.biases = meshgrid(self.weight_space, self.bias_space)
            
            print("PROC CALC:\tCalculate weight and bias space finished")
            print(f"weight space: {self.weight_space}")
            print(f"bias space:   {self.bias_space}")
            
        def approximations_and_mses(self):
            print("PROC CALC:\tCalculate approximations and MSEs for multiple weights and biases")
                    
            mses = []
            sample_values = self.samples[:, 0]
            sample_co_values = self.samples[:, 1]
            
            for i in range(len(self.biases)):
                bias_i = self.biases[i]
                #print(f"bias: {bias_i}")
                bias_i = bias_i[0]
                mses_bias_i = []
                for weight_ij in self.weights[i]:
                    #print(f"weight: {weight_ij}")
                    # calculate approximations
                    approximations_bias_i_weight_ij = self.logistic(weight_ij, sample_values, bias_i)
                    
                    # calculate errors
                    errors_bias_i_weight_ij = approximations_bias_i_weight_ij - sample_co_values
                    mse_bias_i_weight_ij = dot(errors_bias_i_weight_ij, errors_bias_i_weight_ij)
                    mses_bias_i.append(mse_bias_i_weight_ij)
                print(f"\nbias: {bias_i}, weights: {self.weights[i]}, mses: {mses_bias_i}")
                mses.append(mses_bias_i)
                
            self.mses = array(mses)    

        def sample_span(self):
            """
            get first column of samples, which is the domain value
            https://stackoverflow.com/questions/4455076/how-do-i-access-the-ith-column-of-a-numpy-multidimensional-array
            
            calc min, max
            """
            print("PROC CALC:\tCalculate sample span")            
            values = self.samples[:, 0] # all rows, first column            
            return min(values), max(values)
        
        def logistic(self, weight, value, bias):
            """
            Logistic function in one dimensional case 
            https://en.wikipedia.org/wiki/Logistic_function
            """
            return 1 / (1 + exp(-(weight * value + bias)))
    
    def calculate(self):
        """
        Delegates to Proto.Calc, see details there
        """
        print("PROC PROTO:\tCalculate NN1 approximations and MSE errors")
        calc = LogisticMSE.Calc(self.samples)
        calc()
        self.weights = calc.weights
        self.biases  = calc.biases
        self.mses    = calc.mses
    
    def plot(self):
        """
        - plot the 2D (weight, bias) diagram
        - display or save as image
        
        https://matplotlib.org/stable/gallery/mplot3d/axlim_clip.html#sphx-glr-gallery-mplot3d-axlim-clip-py
        """
        print("PROC PROTO:\tPlot NN1 2D error diagram")
        
        fig = plt.figure()        
        ax = fig.add_subplot(projection='3d')
        X, Y, Z = self.weights, self.biases, self.mses
        #from matplotlib import cm
        #ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)
        ax.plot_wireframe(X, Y, Z)
        ax.legend(['NN1 MSEs'])
        plt.show()        
        
if __name__ == "__main__":
    LogisticMSE()()