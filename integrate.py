import numpy as np
import scipy.integrate as integrate


# Defining the function to be integrated
def f(x):
    return np.exp(x)


# Defining the lower and upper limits of integration
a = 0
b = 1
n = 50

# Creating an array of x values from a to b with n subintervals
x_val = np.linspace(a, b, n + 1)

# Evaluate the function at x values
y_val = f(x_val)


trap = integrate.trapezoid(y_val, x_val)  # Using trapezoidal rule
simp = integrate.simpson(y_val, x_val)  # Using Simpson's rule


# Print the results
print("Trapezoidal rule:", trap)
print("Simpson's rule:", simp)
romb = integrate.romberg(f, a, b, show = True)  # Using Romberg method
print("Romberg method:", romb)
