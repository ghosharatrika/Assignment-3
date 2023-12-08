# This code calculates the roots of the function f(x) using secant method

import numpy as np
from scipy import optimize


def f(x):
    return np.sin(np.cos(np.exp(x))) # defining the function


root = optimize.newton(f, -0.1)
print(f"Root for f(x) = sin(cos(exp(x))) with initial value -1 : ", root)
