# this code calculates f(0.45) by fitting curve using lagrange polynomial

#------------------------------------------------------------------------------
# First Function 

import numpy as np
from scipy.interpolate import lagrange

# Given data
x = np.array([0, 0.6, 0.9])
y = np.cos(x)

x_interpolation = 0.45  # Data point for interpolation
polynomial_coeff = lagrange(x, y)  # Calculating Lagrange interpolation polynomial

result = polynomial_coeff(x_interpolation)  # Evaluating the interpolation polynomial at x_interpolation

true_value = np.cos(x_interpolation)  # Calculating the true value of f(0.45)
absolute_error = np.abs(result - true_value)  # Calculating the absolute error

# printing the results
print("Interpolation result:", result)
print("True value:", true_value)
print("Absolute error:", absolute_error)

#------------------------------------------------------------------------------
# Second function 

def f(x):
    return (1+x)**0.5


# Given data
x = np.array([0, 0.6, 0.9])
y = f(x)

x_interpolation = 0.45  # Data point for interpolation
polynomial_coeff = lagrange(x, y)  # Calculating Lagrange interpolation polynomial

result = polynomial_coeff(x_interpolation)  # Evaluating the interpolation polynomial at x_interpolation

true_value = f(x_interpolation)  # Calculating the true value of f(0.45)
absolute_error = np.abs(result - true_value)  # Calculating the absolute error

# printing the results
print("Interpolation result:", result)
print("True value:", true_value)
print("Absolute error:", absolute_error)


#------------------------------------------------------------------------------
# Third Function 

def g(x):
    return np.log(1+x)


# Given data
x = np.array([0, 0.6, 0.9])
y = f(x)

x_interpolation = 0.45  # Data point for interpolation
polynomial_coeff = lagrange(x, y)  # Calculating Lagrange interpolation polynomial

result = polynomial_coeff(x_interpolation)  # Evaluating the interpolation polynomial at x_interpolation

true_value = g(x_interpolation)  # Calculating the true value of f(0.45)
absolute_error = np.abs(result - true_value)  # Calculating the absolute error

# printing the results
print("Interpolation result:", result)
print("True value:", true_value)
print("Absolute error:", absolute_error)


#------------------------------------------------------------------------------
# Fouth Function 

def p(x):
    return np.tan(x)


# Given data
x = np.array([0, 0.6, 0.9])
y = f(x)

x_interpolation = 0.45  # Data point for interpolation
polynomial_coeff = lagrange(x, y)  # Calculating Lagrange interpolation polynomial

result = polynomial_coeff(x_interpolation)  # Evaluating the interpolation polynomial at x_interpolation

true_value = p(x_interpolation)  # Calculating the true value of f(0.45)
absolute_error = np.abs(result - true_value)  # Calculating the absolute error

# printing the results
print("Interpolation result:", result)
print("True value:", true_value)
print("Absolute error:", absolute_error)
