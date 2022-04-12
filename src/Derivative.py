from cmath import log
import sympy as sym
x = sym.Symbol('x')
function = x ** 5 + 7 * x ** 4 + log a ** 5
derivitive = sym.diff(function)
print(derivitive)