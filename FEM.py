# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 21:50:29 2014

@author: stephane-j.robin
"""
# FEM METHOD FOR THE EQUATION u''=x2
# Program written Python 3.3
# This program finds the solution of the equation u''=x^2 using the FEM
# We claim to transform the problem into the resolution of the linear problem AX=B

from matplotlib import pyplot as plt
import numpy as np

# DEFINING USEFUL FUNCTIONS
def f(x): # the function given by the studied equation
    return x**2

def F(x,k): # the function such that appears in the integral to calculate Bi
    global h
    return (x-k*h)*f(x)/h
    
def integrale(a,b,k): # calculates the integral of the function F
    I1,I2=0.,0.
    for p in range(0,10000):
        I1=F(a+p*(b-a)/10000.,k)+I1
    I1=I1*(b-a)/10000.
    
    for p in range(1,10001):
        I2=F(a+p*(b-a)/10000.,k)+I2
    I2=I2*(b-a)/10000.
            
    return (I1+I2)/2.

# DEFINING THE STEP OF THE METHOD
n=5

h=float(1/n)

# CREATING MATRIX A
A=2*np.eye(n,n)
for i in range(0,n-1):
    A[i][i+1]=1
for i in range(1,n):
    A[i][i-1]=1
A=np.dot(n,A)
print ("A=",A)

# SOLVING AX=B
# Calculating matrices L and S by iteration
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

# solving LX=B by iteration climbing up
# B=list(range(0,n)) # initialisation
X=list(range(0,n))
#B[1]=integrale(0,h,0)-integrale(h,2*h,2)
X[1]=h*B[1]/2
for i in range(2,n):
    #B[i]=integrale((i-1)*h,i*h,i-1)-integrale(i*h,(i+1)*h,i+1) # create B_i
    X[i]=(h*B[i]-X[i-1])/2 # create X_i
#print(B)
print(X)

# solving Su=X by iteration climbing down
u=list(range(0,n))
u[n-1]=X[n-1]
for i in range(2,n+1):
   # X=h*B-2*X
    u[n-i]=h*X[n-i+1]-u[n-i+1]

# PRINTING THE SOLUTION u    
for i in range(1,n+1):
    print("u(",i,")= ",u[i-1])
    
# PRINTING THE GRAPH
# Designing the background
plt.figure(1)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.xlim(0,1) # the interval of study is [0,1]
plt.ylim(-2,2)
X00=np.zeros(50)
Y00=np.linspace(-2,2,50)
plt.title("Resolution of $ \Delta u(x)=x^2 $, by the finite elements method")
X0=np.linspace(0,1,50)
Y0=np.zeros(50)
plt.plot(X00,Y00,'k',X0,Y0,'k',linewidth=1)

# Designing the theoretical solution
t=np.linspace(0,1,50)
ut=t+t**4/12
plt.plot(t,ut,'r',linewidth=2)


#i=linspace()
#plt.plot(i,u,'g',linewidth=2)

for i in range(0,n-3):
    plt.plot([i*h,u[i]],[(i+1)*h,u[i+1]],'g',linewidth=2)
    
plt.show()
    
