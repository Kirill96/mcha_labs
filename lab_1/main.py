#The first lab MChA

import lab_1
from sympy import *

menu = int(raw_input("\n1. System 1; \n2. System 2; \n3. System 3; \n4. System 4; \n5. System 5. \n Your choice: "))
if menu == 1:

	A = Matrix([[8, 1, 8], [-1, 8, 1], [8, -1, 8]])
	b = Matrix([10, 17, 6])

	print "\nAnswer: ", lab_1.System(A, b)

elif menu == 2:

	A = Matrix([[4, 3, -2], [1, -2, 1], [2, -3, -4]])
	b = Matrix([12, 9, -6])

	print "\nAnswer: ", lab_1.System(A, b)

elif menu == 3:

	A = Matrix([[2, -3, 0, 1], [3, -2, 1, 2], [1, 1, 1, 1], [-1, 2, -1, 2]])
	b = Matrix([3, 0, 2, 4])

	print "\nAnswer: ", lab_1.System(A, b)

elif menu == 4:

	A = Matrix([[5, -3], [-10, 6]])
	b = Matrix([0, 0])

	print "\nAnswer: ", lab_1.System(A, b)

elif menu == 5:

	print "\nAnswer: "
	lab_1.System_5()