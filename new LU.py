# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 17:34:28 2014

@author: stef
"""
# FEM METHOD FOR THE EQUATION u''=exp(x)
# Program written Python 3.3
# This program finds the solution of the equation u''=exp(x) using the FEM
# We claim to transform the problem into the resolution of the linear problem
# Auh=B which would give us an approximation of the solution

# DEFINING THE FUNCTION GIVEN BY THE EQUATION
def f(x): 
    return exp(x)
# ====================================================================
    
# DEFINING THE STEP OF THE METHOD
n=5
h=float(1/n)
# ====================================================================

# CREATING MATRIX A

A=-2*eye(n,n) # initialisation

for i in range(0,n-1): # calculating Aij
    A[i,i+1]=1
for i in range(1,n):
    A[i,i-1]=1
A=dot(n,A)

print(A) # TEST
# =====================================================================

# CREATING VECTOR B

B=zeros((n,1)) #list(range(0,n)) # initialisation

def F(y,k): # defining the function in the integral to calculate Bi
    global h
    return (y-k*h)*f(y)
    
def integrale(a,b,k): # calculating the integral of the function F
    I1,I2=0.,0.
    for i in range(0,10000):
        I1=F(a+i*(b-a)/10000.,k)+I1
    I1=I1*(b-a)/10000.
    for i in range(1,10001):
        I2=F(a+i*(b-a)/10000.,k)+I2
    I2=I2*(b-a)/10000.
    return (I1+I2)/2.
    
for i in range(1,n): # calculating Bi
    B[i-1]=n*integrale((i-1)*h,i*h,i-1)-n*integrale(i*h,(i+1)*h,i+1)

print(B) # TEST
# ======================================================================

# SOLVING AX=B
# Calculating matrices L and S by iteration
L=eye(n,n) # we give a neutral value to L
for k in range(1,n): # k is defined between 1 and n-1 (n-1 iterations are necessary)
    M=eye(n,n)    
    for i in range(k,n): # changing matrix Lk
        M[i,k-1]=-(A[i,k-1])/(A[k-1,k-1])
    A=dot(A,M) # defining the new value for A putting 0 under some terms of the diagonal after each iteration
    invM=linalg.inv(M) # defining the inverse of Lk after each iteration
    L=dot(L,invM) # defining L after each iteration as the product of inverse matrices Lk
S=A # defining S as A after n-1 iterations, i.e S is the product of matrices Lk and A
print("S=",S)
print("L=",L)  

# solving LX=B by iteration climbing up
# initialisation
X=list(range(0,n))
X[0]=h*B[0]/2
for i in range(1,n):
    X[i]=(h*B[i]-X[i-1])/2 # create X_i
print(X)

# solving Su=X by iteration climbing down
ut=list(range(0,n))
ut[n-1]=X[n-1]
for i in range(2,n+1):
   # X=h*B-2*X
    ut[n-i]=h*X[n-i+1]-ut[n-i+1]
    
uh=list(range(0,n+1)) # finding the approximated solution & fitting it to the end of interval
# uh is a vector size n+1 (useful for the graph to finish at the end of the interval) 
for i in range(1,n+1):
    uh[i]=ut[i-1]

def u(x): # Designing the theoretical solution
    return exp(x)+(1-exp(1))*x-1

uh[0]=u(0)

for i in range(0,n+1): # printing the approximated solution uh
    print("uh[",i,"]=",uh[i]) 

for i in range(0,n+1): # printing the solution u
    print("u[x",i,"]=",u(i*h)) 
# ======================================================================

# PRINTING THE GRAPH

x=list(range(0,n+1)) # defining coordinates of the knots
for i in range(0,n+1):
    x[i]=i*h

plt.figure(1) # Designing the background
plt.title("Resolution of $ \Delta u(x)=e^x $, by the FEM, step h=0.02")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.xlim(0,1) # (the interval of study is [0,1])
plt.ylim(-0.3,0.3)

X1=np.linspace(0,1,50) # designing X axis 
X2=np.zeros(50)

Y1=np.zeros(50) # designing Y axis
Y2=np.linspace(-0.3,0.3,50)

plt.plot(X1,X2,'k',Y1,Y2,'k',linewidth=1)# printing the axis

plt.plot(x,uh,'b',linewidth=2) # printing the graph of the approximated solution in blue

t=np.linspace(0,1,50) # printing the graph of the theoretical solution in red
plt.plot(t,u(t),'r',linewidth=2)

plt.show()



