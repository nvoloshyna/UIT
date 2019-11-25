import autograd.numpy as np
import autograd
def newton(f, x0, tol=1.48e-08, maxiter=50):
    g = autograd.grad(f)
    h = autograd.hessian(f)
    x = x0
    for _ in range(maxiter):
        delta = np.linalg.solve(h(x), -g(x))
        x = x + delta
        if np.linalg.norm(delta) < tol:
            break
    return x
def main():
    def f(x):
        return (x[0] - 4)**2 + (x[1] - 4/2)**2 - x[0]*x[1]/ 414
    x0 = np.array([1., 1.])
    print(newton(f, x0))
