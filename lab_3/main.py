#The 3nd lab MChA

import lab_3
import numpy as numpy
import sympy as sympy

menu = int(raw_input("1. Count of solutions.\n2. Intervals with one solution.\n3. Method pol.delen and method hord.\nYour choice: "))
print "\nx^3 + ax^2 + bx + c = 0"
if menu == 1:
    print "\nCount of solutions =  ", lab_3.task_1()
elif menu == 2:
    print "\n Intervals with one solution:\n"
    print lab_3.task_2()
elif menu == 3:
    print "\n Method pol.delen and method hord:\n"
    print lab_3.task_3()
    