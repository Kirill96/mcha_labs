from sympy import *

a = 20.2374
b = -131.210
c = -843.923
e = 0.0001

list_shturm = []

x = Symbol('x')
fx = x**3 + a*x**2 + b*x + c
df = diff(fx, x)
list_sol = []

def task_1():

    list_shturm.append(fx)
    list_shturm.append(df)
    f = prem(fx, df)
    list_shturm.append(f)
    list_shturm.append(prem(df, f))
    Na = [elem.subs(x, -10.0) for elem in list_shturm]
    Nb = [elem.subs(x, 10.0) for elem in list_shturm]
    number_of_solutions = 0

    for i in range(1, len(list_shturm)):
        if Na[i-1]*Na[i] < 0:
            number_of_solutions += 1
        if Nb[i-1]*Nb[i] < 0:
            number_of_solutions -= 1

    return number_of_solutions    

def less_of_interval(x1, x2):
    if (x2 - x1) > 3:
        x0 = (x2 + x1) / 2
        if fx.subs(x, x1) * fx.subs(x, x0) < 0:
            return less_of_interval(x1, x0)
        elif fx.subs(x, x2) * fx.subs(x, x0) < 0:
            return less_of_interval(x0, x2)
        else:
            return [x1, x2]
    else:
        return [x1, x2]

def task_2():
    task_1()
    k = [el for el in solve(Eq(df, 0), x) if (el < 10 and el > -10)]
    if len(k) == 1:
        x0 = k[0]
        if (fx.subs(x, -10.0) * fx.subs(x, x0) < 0):
            val = less_of_interval(-10.0, x0)
            list_sol.append(val)
            print "  [", val[0], "; ", val[1], "]"
        if (fx.subs(x, 10.0)*fx.subs(x, x0) < 0):
            val = less_of_interval(x0, 10.0)
            list_sol.append(val)
            print "  [", val[0], "; ", val[1], "]"        

def task_3():
    task_1()
    task_2()
    xk = [list_sol[0][1], list_sol[0][0]]
    n = 0
    while (((xk[0] - xk[1]) > e) or ((xk[1] - xk[0]) > e)):
        n += 1
        m = (xk[0] + xk[1]) / 2
        if fx.subs(x, m)*fx.subs(x, xk[0]) < 0:
            xk[1] = m
        else:
            xk[0] = m

    print "Method pol.del.:\nMin answer =  ", (xk[0]+xk[1]) / 2, "; ", n, "iterations."

    xk = [list_sol[0][1], list_sol[0][0]]
    x_0 = xk[0]
    n = 0
    while (((x_0 - xk[1]) > e) or ((xk[1] - x_0) > e)):
        n += 1
        x_0 = xk[1]
        xk[1] = xk[0] - fx.subs(x, xk[0])/(fx.subs(x, xk[1]) - fx.subs(x, xk[0]))*(xk[1] - xk[0])

    print "\nMethod hord:\nMin answer = ", xk[1], "; ", n, "iterations."
