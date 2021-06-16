# Function drawing
# program written in Python 2.7

# Importing useful packages
from matplotlib import pyplot as plt
import numpy as np

# Creating the function
def f(x):
	return -2*x*np.exp(-x*x)   # IT IS REQUIRED TO CHANGE THE FUNCTION

# Designing the background
plt.figure(1)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
print "The graph will be drawn for a specific interval"
a=input("Please enter the minimum in this interval : ")
b=input("Please enter the maximum in this interval : ")
plt.title(r"$ x'=-2 t x $")  # IT IS REQUIRED TO CHANGE THE FUNCTION
xX=np.zeros((abs(a)+b)*10)  # designing x axis
yX=np.linspace(f(a),f(b),(abs(a)+b)*10)
xY=np.linspace(a,b,(abs(a)+b)*10) # designing y axis
yY=np.zeros((abs(a)+b)*10)
plt.plot(xX,yX,'k',xY,yY,'k',linewidth=1)

# Designing the function
x=np.linspace(a,b,(abs(a)+b)*10)
plt.plot(x,f(x),'g',linewidth=2)

plt.show()

