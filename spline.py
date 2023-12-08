# This code does a spline fitting to a set of data points

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

#Data points
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([1.0, 2.0, 1.0, 0.5, 4.0, 8.0])

# Fit a linear spline
spl1 = InterpolatedUnivariateSpline(x, y, k=1)

# Fit a quadratic spline
spl2 = InterpolatedUnivariateSpline(x, y, k=2)

# Fit a cubic spline
spl3 = InterpolatedUnivariateSpline(x, y, k=3)

# Evaluate the splines on a finer grid
x_range = np.arange(0, 5.01, 0.01)
ys1 = spl1(x_range)
ys2 = spl2(x_range)
ys3 = spl3(x_range)

# Plotting the data and the splines
plt.plot(x, y, 'o')
plt.plot(x_range, ys1)
plt.plot(x_range, ys2)
plt.plot(x_range, ys3)
plt.legend(['True Data', 'Linear', 'Quadratic spline', 'Cubic Spline'])
plt.title('Spline Interpolation')
plt.show()
