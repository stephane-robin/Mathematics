# Euler method

# Importing useful packages
from matplotlib import pyplot as plt
import numpy as np
import os

# Designing the background
plt.figure(1)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.xlim(-2,12)
plt.ylim(-10,30)
X00=np.zeros(100)
Y00=np.linspace(-10,30,100)
plt.title(r"$ y=1/3 e^{x/2} $, Approximation by Euler's method")
X0=np.linspace(-2,12,100)
Y0=np.zeros(100)
plt.plot(X00,Y00,'k',X0,Y0,'k',linewidth=1)

# Designing the function
t=np.linspace(0,10,100)
x=(np.exp(t/2))/3
plt.plot(t,x,'g',linewidth=2)

# Designing the approximation
k=1
n=input("Please enter the number of iterations : ")
xk=1./3

while k<n:
	plt.plot([x],[y],'r')
	xk=xk*(1+5/n)
	k=k+1

# Printing
plt.show()

