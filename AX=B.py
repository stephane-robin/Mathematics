# RESOLUTION OF A SYSTEM
# Program written Python 3.3
# This program finds the solution of a system such as AX=B with the LU decomposition

# Introduction
print ("- RESOLUTION OF A SYSTEM -")
print (" ")
print ("This program finds the solution of a system such as AX=B with the LU decomposition.")

import numpy as np
# DEFINING THE STEP
n=5
h=float(1/n)

# CREATING MATRIX A
A=2*np.eye(n,n)
for i in range(0,n-1):
    A[i][i+1]=1
for i in range(1,n):
    A[i][i-1]=1
print ("A=",A)

# CREATING MATRIX B


# CALCULATING MATRICES L AND U BY ITERATION
L=np.eye(n,n) # we give a neutral value to L
for k in range(1,n): # k is defined between 1 and n-1 (n-1 iterations are necessary)
    M=np.eye(n,n)    
    for i in range(k,n): # changing matrix Lk
        M[i][k-1]=-(A[i][k-1])/(A[k-1][k-1])
    A=np.dot(M,A) # defining the new value for A putting 0 under some terms of the diagonal after each iteration
    invM=np.linalg.inv(M) # defining the inverse of Lk after each iteration
    L=np.dot(L,invM) # defining L after each iteration as the product of inverse matrices Lk
S=A # defining S as A after n-1 iterations, i.e S is the product of matrices Lk and A
print("S=",S)
print("L=",L)  




