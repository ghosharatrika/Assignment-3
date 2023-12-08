# This code calculates the integral using composite simpson rule

import numpy as np
import math as mp


def f(x):
    return np.tan(x)


a = 0  # Lower Limit of integration
b = 3*mp.pi/8  # Upper Limit of integration
n = 8  # No. of evaluation


def simpsons_rule(f, a, b, n):
    h = (b - a) / n  # Step size
    k = 0.0
    x = a + h
    for i in range(1, int(n/2 + 1)):
        k += 4*f(x)
        x += 2*h

    x = a + 2*h
    for i in range(1, int(n/2)):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)


result = simpsons_rule(f,a,b,n)
print("Function f(x) = tan(x)")
print(f"Integration using composite simpson rule for n = {n} : {result}")

#----------------------------------------------------------------
# Second Function

def f(x):
    return 2/(x**2+4)


a = 0  # Lower Limit of integration
b = 2  # Upper Limit of integration
n = 6  # No. of evaluation


def simpsons_rule(f, a, b, n):
    h = (b - a) / n  # Step size
    k = 0.0
    x = a + h
    for i in range(1, int(n/2 + 1)):
        k += 4*f(x)
        x += 2*h

    x = a + 2*h
    for i in range(1, int(n/2)):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)


result = simpsons_rule(f,a,b,n)
print("Function f(x) = 2/(x^2+4)")
print(f"Integration using composite simpson rule for n = {n} : {result}")


#----------------------------------------------------------------
# First Function


def f(x):
    return x*np.log(x)


a = 1  # Lower Limit of integration
b = 2  # Upper Limit of integration
n = 4  # No. of evaluation


def simpsons_rule(f, a, b, n):
    h = (b - a) / n  # Step size
    k = 0.0
    x = a + h
    for i in range(1, int(n/2 + 1)):
        k += 4*f(x)
        x += 2*h

    x = a + 2*h
    for i in range(1, int(n/2)):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)


result = simpsons_rule(f,a,b,n)
print("Function f(x) = x ln(x)")
print(f"Integration using composite simpson rule for n = {n} : {result}")

