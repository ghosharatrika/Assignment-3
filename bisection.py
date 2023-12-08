# This code calculate the root of the function using bisection method

import numpy as np
from scipy import optimize


def f(x):
    return np.sin(np.cos(np.exp(x))) # defining the function


root = optimize.bisect(f, -1, 1)
print("Roots between -1 and 1: ", root)
print(f"Value of f(x) = sin(cos(exp(x))) at x = {root}: {f(root)}")
