# This code calculates the root of the function using Newton Rapshon method

import numpy as np
from scipy import optimize


def f(x):
    return np.sin(np.cos(np.exp(x)))


def derivative_f(x):
    return -np.exp(x)*np.cos(np.cos(np.exp(x)))*np.sin(np.exp(x))


root = optimize.newton(f, -1.0, derivative_f)
print(f"Root for f(x) = sin(cos(exp(x))) with initial value -1 : ", root)
root = optimize.newton(f, -0.1, derivative_f)
print(f"Root for f(x) = sin(cos(exp(x))) with initial value -0.1 : ", root)
