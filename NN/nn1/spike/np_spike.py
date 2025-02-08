from numpy import exp, array

def logistic(value, weight, bias):
    return 1 / (1 + exp(weight * value + bias))
    
values = array([-1,0,1])
weight = 0.5
bias = -1

logistics = logistic(values, weight, bias)

for i in range(values.size):
    print(f"{values[i]} -logistic({weight} * v + {bias})-> {logistics[i]}")