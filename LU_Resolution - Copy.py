# FEM METHOD FOR THE EQUATION u''=exp(x)
# Program written Python 3.3
# This program finds the solution of the equation u''=exp(x) using the FEM
# We claim to transform the problem into the resolution of the linear problem
# Auh=B which will give us an approximation of the solution

# DEFINING THE FUNCTION GIVEN BY THE EQUATION
def f(x): 
    return exp(x)
# ====================================================================

# DESIGNING THE THEORETICAL SOLUTION
def u(x):
    return exp(x)+(1-exp(1))*x-1    
# ====================================================================
    
# DEFINING THE NUMBER OF ITERATIONS (linked to the step)
n=7
# ====================================================================

# CREATING MATRIX A

A=-2*eye(n-1,n-1) # initialisation, A is a matrix size n-1

for i in range(0,n-2): # calculating Aij
    A[i,i+1]=1
for i in range(1,n-1):
    A[i,i-1]=1
A=dot(n,A)

print(A) # TEST
# =====================================================================

# CREATING VECTOR B

B=zeros((n-1,1)) # initialisation, B is a vector size n-1

def F(y,k): # defining the function in the integral to calculate Bi
    global n
    return (y-k/n)*f(y)
    
def integrale(a,b,k): # calculating the integral of the function F
    I1,I2=0.,0.
    for i in range(0,10000):
        I1=F(a+i*(b-a)/10000.,k)+I1
    I1=I1*(b-a)/10000.
    for i in range(1,10001):
        I2=F(a+i*(b-a)/10000.,k)+I2
    I2=I2*(b-a)/10000.
    return (I1+I2)/2.
    
for i in range(1,n-1): # calculating Bi
    B[i-1]=n*integrale((i-1)/n,i/n,i-1)-n*integrale(i/n,(i+1)/n,i+1)

print(B) # TEST
# ======================================================================

# SOLVING A.uh=B
ut=linalg.solve(A,B) # using a temporary variable to calculate the approximated solution
                     # ut is a vector size n-1 giving the value of the knots inside the interval
                     # ut has the same size as A and B

uh=list(range(0,n+1)) # finding the approximated solution by fitting it to the boundaries of the interval
                      # uh is a vector size n+1 
for i in range(1,n):
    uh[i]=ut[i-1]
uh[0]=0
uh[n]=0

for i in range(0,n+1): # printing the approximated solution uh
    print("uh[",i,"]=",uh[i]) 

for i in range(0,n+1): # printing the solution u
    print("u[x",i,"]=",u(i/n)) 
# ======================================================================

# PRINTING THE GRAPH

x=list(range(0,n+1)) # defining coordinates of the knots
for i in range(0,n+1):
    x[i]=i/n
print(x)

plt.figure(1) # Designing the background
plt.title("Resolution of $ \Delta u(x)=e^x $, by the FEM, step h=0.16")
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



