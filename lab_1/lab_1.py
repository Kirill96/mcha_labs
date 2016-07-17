from sympy import *

def System(A, b):
    """lab_1"""
	for elem in range(A.rows - 1):

		if A[elem, elem] == 0:
			temp = b[elem]
			b[elem] = b[elem + 1]
			b[elem + 1] = temp

			for _elem in range(3):
				temp = A[elem, _elem]
				A[elem, _elem] = A[elem + 1, _elem]
				A[elem + 1, _elem] = temp

		for i in range(elem + 1, A.rows):
			a = A[i, elem]
			b[i] = b[i] - b[elem]*a/A[elem, elem]

			for j in range(elem, A.cols):
				A[i, j] = A[i, j] - A[elem, j]*a/A[elem, elem]

	x = [Symbol("x" + str(i)) for i in range(1, A.cols + 1)]

	for i in range(A.rank() - 1, -1, -1):
	    x[i] = b[i]

	    for j in range(A.cols - 1, i, -1):
	        x[i] -= A[A.cols * i + j] * x[j]

	    x[i] /= A[A.cols * i + i]

	return x

def System_5():
	
	a = Symbol("a")
	A = Matrix([[1, 5, 1], [a, -3, -7], [3, a, -6]])
	b = Matrix([0, 0, 0])
	values_a = solve(Eq(A.det(), 0), a)
	
	print values_a

	for value in values_a:
		solve_values_a = System(A.subs(a, value), b)
		print "a = ", value, "\nSolve: ", solve_values_a


