# this code calculate R 3,3 

from scipy.integrate import romberg
import numpy as np
import math as mp

#--------------------------------------
# First Function

def f(x):
    return x ** 2* np.log(x)


# Integration limits
a = 1
b = 1.5
result = romberg(f, a, b, divmax=3, show=True)  # Using Romberg integration with divmax=3 to get R3,3

print(f"Result of the Romberg integration (order 3): {result}")



#--------------------------------------
# Second Function

def f(x):
    return x ** 2* np.exp(-x)


# Integration limits
a = 0
b = 1
result = romberg(f, a, b, divmax=3, show=True)  # Using Romberg integration with divmax=3 to get R3,3

print(f"Result of the Romberg integration (order 3): {result}")

#--------------------------------------
# Third Function

def f(x):
    return np.cos(x) ** 2


# Integration limits
a = 0
b = mp.pi/4
result = romberg(f, a, b, divmax=3, show=True)  # Using Romberg integration with divmax=3 to get R3,3

print(f"Result of the Romberg integration (order 3): {result}")
