#The 2nd lab MChA

import lab_2
import numpy as numpy
import sympy as sympy

A = numpy.array([[40.41, 2.42, 3.86],
                 [2.31, 21.49, 4.55], 
                 [2.49, 4.85, 25.96]])
b = numpy.array([20.41, 30.11, 12.24])

menu = int(raw_input("1. Method Simple Iter.\n2. Method Zeydel.\nYour choice: "))
if menu == 1:
    print "\nMethod Simple Iterations: "
    print lab_2.met_sim_iter(A, b)
elif menu == 2:
    print "\nMethod Zeydel: "
    print lab_2.met_zeyd(A, b)
