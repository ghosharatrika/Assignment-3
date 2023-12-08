import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

# Given data
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([1.0, 2.0, 1.0, 0.5, 4.0, 8.0])

# Using Lagrange's method to find the fifth-order polynomial
fifth_order_poly = lagrange(x, y)

# Generate points for smoother plotting
x_range = np.arange(0, 5.01, 0.01)
y_range = fifth_order_poly(x_range)

# Plot the results
plt.scatter(x, y, label='Data points')
plt.plot(x_range, y_range, color='red')
plt.legend(['Data points', 'Fifth-order Polynomial'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fifth-order Polynomial Interpolation')
plt.show()
