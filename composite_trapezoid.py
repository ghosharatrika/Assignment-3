# This code calculates the integral of three function using composite trapezoidal rule

import numpy as np
import math as mp

# Defining the first function
def f(x):
    return x*np.log(x)

a = 1  # Lower Limit of integration
b = 2  # Upper Limit of integration
n = 4  # No. of evaluation
h = (b-a)/n  # Step size
trap = 0.0

for i in range(1, n):
    trap += f(a+i*h)

trap += (f(a)+f(b))/2.0
trap = trap*h
print(f"Integration using trapezoidal rule for n = {n} : {trap}")

#-------------------------------------------------------------------------------
# Defining the second function

def g(x):
    return 2/(x**2+4)


a = 0  # Lower Limit of integration
b = 2  # Upper Limit of integration
n = 6  # No. of evaluation
h = (b-a)/n  # Step size
trap = 0.0

for i in range(1, n):
    trap += g(a+i*h)

trap += (g(a)+g(b))/2.0
trap = trap*h
print(f"Integration using trapezoidal rule for n = {n} : {trap}")

#-------------------------------------------------------------------------------
# Defining the third function

def p(x):
    return np.tan(x)


a = 0  # Lower Limit of integration
b = 3*mp.pi/8  # Upper Limit of integration
n = 8  # No. of evaluation
h = (b-a)/n  # Step size
trap = 0.0

for i in range(1, n):
    trap += p(a+i*h)

trap += (p(a)+p(b))/2.0
trap = trap*h
print(f"Integration using trapezoidal rule for n = {n} : {trap}")
