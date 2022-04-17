import numpy as np 
from sympy import Symbol 

a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
d = Symbol('d')
e = Symbol('e')
f = Symbol('f')
g = Symbol('g')
h = Symbol('h')
i = Symbol('i')

M1 = np.array([[3,0,3],[1,1,0]])

M2 = np.array([[4,4],[0,1],[4,1]])

#print(M1 @ M2)

M3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
M4 = np.array([[a,b,c],[d,e,f],[g,h,i]])

M5 = np.array([[2,-4,10],[2,3,-4],[4,2,0]])
M6 = np.array([[1,5,8],[4,4,5],[8,12,1]])

M7 = np.array([[1,2,5],[3,4,4],[5,9,1]])

M8 = np.array([[1,1,1],[2,2,2],[3,3,0]])

M9 = np.array([[11,12,13],[7,12,31],[12,18,61]])

M10 = np.array([[0,0,13],[0,0,31],[0,0,61]])

#print(M3 @ M4)

r = np.linalg.matrix_rank(M10)

print("The rank of the matrix is ", r)
