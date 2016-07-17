import numpy as numpy
import sympy as sympy

def met_sim_iter(A, b):
    C, d = iteration_view(A, b)
    print "\nx = Cx + d\n"
    print "C = \n", C, "\n", "\nd = \n", d
    print "\nConvergence: ", convergence_msi(C)
    if convergence_msi(C):
        x0 = numpy.ones(3)
        x1 = numpy.dot(C, x0) + d
        while any(x1 - x0 > 0.00001) or any(x0 - x1 > 0.00001):
            x0 = x1
            x1 = numpy.dot(C, x0) + d
        print "\nSolution:"

    return x1


def met_zeyd(A, b):
    C, d = iteration_view(A, b)
    H = sympy.zeros(3)
    F = sympy.zeros(3)
    c = sympy.zeros(3,1)
    for i in xrange(3):
        c[i] = d[i]
        for j in xrange(3):
            if i > j:
                H[i, j] = C[i, j]
            else:
                F[i, j] = C[i, j]
    print "\nx = Cx + d\n"
    print "C = \n", C, "\n", "\nd = \n", d
    print "\nConvergence: ", convergence_mzeyd(C, d)
    if convergence_mzeyd(C, d):
        E = sympy.eye(3)
        x0 = sympy.ones(3, 1)
        x1 = (E-H).inv()*F*x0 + (E-H).inv()*c
        while ((x1-x0)[0] > 0.00001 or (x1-x0)[1] > 0.00001 or\
              (x1-x0)[2] > 0.00001 or (x0-x1)[0] > 0.00001 or\
              (x0-x1)[1] > 0.00001 or (x0-x1)[2] > 0.00001):
              x0 = x1
              x1 = (E-H).inv()*F*x0 + (E-H).inv()*c
        print "\nSolution:" 

    return [element for element in x1]


def iteration_view(A, b):
    C = numpy.zeros((3, 3))
    d = numpy.zeros(3)
    for i in xrange(3):
        d[i] = b[i] / A[i, i]
        for j in xrange(3):
            if i != j:
                C[i, j] = -A[i, j] / A[i, i]

    return C, d


def convergence_msi(C):
    l, v = numpy.linalg.eig(C)
    convergence = True
    for element in l:
        convergence = convergence and (-1 < element < 1)
    if convergence:
        return True
    else:
        return False


def convergence_mzeyd(C, d):
    H = sympy.zeros(3)
    F = sympy.zeros(3)
    c = sympy.zeros(3,1)
    for i in xrange(3):
        c[i] = d[i]
        for j in xrange(3):
            if i > j:
                H[i, j] = C[i, j]
            else:
                F[i, j] = C[i, j]
    x = sympy.Symbol('x')
    T = F + x*H + x*sympy.eye(3)
    x_res = sympy.solve(sympy.Eq(T.det(), 0), x)
    convergence = True
    for element in x_res:
        convergence = convergence and (-1 < element < 1)
    if convergence:
        return True
    else:
        return False
