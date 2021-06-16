# Title : Newton's method
# To read : this program gives a zero of a function providing the function is differentiable with a derivative that doesn't get nul.
# It is necessary to change the definition of the function F and its derivative function f in the program before running it.
# warning : this method is very unstable and it is necessaty to choose an initial value close to a zero in order to find it. It is hence necessary to check every result.
# program written in python 2.7

print "- Newton's method -"
print "  "
print "This program gives a zero of a function providing the function is differentiable with a derivative that doesn't get nul. It uses the Newton's method which is very unstable and it is necessary to choose an initial value close to a zero in order to find it. It is hence necessary to check every result."
print "  "

# importing useful packages
import os
import numpy as np
import math

# defining useful functions
def F(x): # function which zero we are looking for
	return x**2-3
	#return np.cos(x)-x**3

def f(x): # derivative function of F
	return 2*x
	#return -np.sin(x)-3*x**2
	
# defining useful variables
x0=input("Please enter the initial value : ")
n=input("Please enter the number of iterations : ")
k=0
x=float(x0)

# defining the sequence from Newton's method
while k<n:
	x=x-F(x)/f(x)
	k=k+1
	print x,

# showing the result
print "a zero of the function is : ",x

os.system("pause")
