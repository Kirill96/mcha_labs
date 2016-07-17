from sympy import *

def MSI():

    a = 0.6
    m = 0.3
    e = 0.0001
    x = Symbol('x')
    y = Symbol('y')
    X = sqrt((1-2*y**2)/a)
    Y = (atan(x) - m) / x
    x0, y0 = 0.9, 0.5
    x1, y1 = X.subs(x, x0).subs(y, y0), Y.subs(x, x0).subs(y, y0)
    n = 1
    while (abs(x0 - x1) > e or abs(y0 - y1) > e):
	   x0, y0 = x1, y1
	   x1, y1 = X.subs(x, x0).subs(y, y0), Y.subs(x, x0).subs(y, y0)
	   n += 1

    return 'Solution: x = ', x1, ' y = ', y1, ' n = ', n

def NewtonM():
    
    a = 0.6
    m = 0.3
    e = 0.0001
    x = Symbol('x')
    y = Symbol('y')
    X = sqrt((1-2*y**2)/a)
    Y = (atan(x) - m) / x
    f1 = tan(x*y + m) - x
    f2 = a*x**2 + 2*y**2 - 1
    F = Matrix([f1, f2])
    J = Matrix([[diff(f1, x), diff(f1, y)], [diff(f2, x), diff(f2, y)]])
    v0 = Matrix([0.9, 0.5])
    J = J.inv()
    v1 = (v0 - J.inv()*F).subs(x, v0[0]).subs(y, v0[1])
    n = 1

    while (abs(v0[0] - v1[0]) > e or abs(v0[1] - v1[1]) > e):
    	v0 = v1
    	v1 = (v0 - J*F).subs(x, v0[0]).subs(y, v0[1])
    	n += 1

    return 'Solution: x = ', v1[0], ' y = ', v1[1], ' n = ', n