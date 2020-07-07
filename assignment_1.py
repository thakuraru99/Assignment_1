#Code by Arunima Thakur
#ASSIGNMENT-1
#PROBLEM- Draw two triangles having same base between two parallel lines.

import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#if using termux
import subprocess
import shlex
#end if

#Generating the parallel lines
plt.plot([-2,7],[3.3,3.3])
plt.plot([-2,7],[0,0])
#sides of triangle ABC
a = 6
b = 5
c = 4

#Coordinates of A
p = (a**2 + c**2-b**2 )/(2*a)
q = np.sqrt(c**2-p**2)
print(p,q)
#Triangle vertices
A = np.array([p,q]) 
B = np.array([0,0]) 
C = np.array([a,0]) 

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')

# Sides of the triangle DBC
a=6
d=4
h=5

#Coordinates of D
r = (a**2 + h**2-d**2 )/(2*a)
s= np.sqrt(h**2-r**2)
print(r,s)

#vertices of triangle DBC
D=np.array([r,s])
B=np.array([0,0])
C=np.array([a,0])

#Generating all the lines of traingle
x_DB = line_gen(D,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)

#Plotting all lines
plt.plot(x_DB[0,:],x_DB[1,:],label='$DB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')

plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.1), D[1] * (1 - 0.1) , 'D')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()
plt.show()
plt.show()


