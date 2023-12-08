# In this code i have written newton rapshon algorithm

def newton_raphson(f, f_derivative, x0, tolerance=1e-6, max_iter=30):

  """
  f: function whose root is to be found
  f_derivative: derivative of the function
  x0: initial guess for the root
  tolerance: Small value to compare if f'(x) with zero and also to approximate the root
  max_iter: maximum no. of iterations allowed

  Outputs:
  x: approximate root of the function
  (i+1): total no. of iterations required to find the root

  """
    x = x0
    for i in range(max_iter):
        f_value = f(x)
        f_derivative_value = f_derivative(x)

        # Check for division by zero
        if abs(f_derivative_value) < tolerance:
            raise ValueError("Derivative is close to zero. Newton-Raphson method cannot continue.")

        x -= f_value / f_derivative_value

        # Check for convergence
        if abs(f_value) < tolerance:
            return x, i + 1

    raise ValueError("Newton-Raphson method did not converge within the specified number of iterations.")

