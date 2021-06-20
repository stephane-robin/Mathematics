# Title : DICHOTOMY
# To read : this program gives the zero of a function
# It is necessary to change the definition of the function f in the program before running it.
# program written in Python 2.7

# IMPORTING USEFUL PACKAGES
import os
import math as m

# MAIN BLOCK

print "- Dichotomy -"
print "  "
print "This program gives a zero of a function. It uses the dichotomy method which is very unstable and runs into an interval. It is hence necessary to previously find an interval encompassing this zero (and only this zero) before starting the algorithm. It is also necessary to check every result."
print "  "

# defining borders of study
a = float(input("Please enter the smallest border of the interval of study : "))
b = float(input("Please enter the biggest border of the interval of study : "))

# defining function f
def f(x):
	return x - 1

def Dichotomy(x, y):                      
	while abs(x - y) >= 0.01:                                    
		if (f(x) * f(y) < 0.) and (f(x) * f((x + y) / 2.) < 0.):
			y = (x + y) / 2.
			                                       
		if (f(x) * f(y) < 0.) and (f((x + y) / 2.) * f(y) < 0.):
			x = (x + y) / 2.
	return (x + y) / 2.

if (f(a) * f(b) > 0):
        print" "
        print"It is necessary that the images of the borders have a different sign."
        print"Please change the interval of study"
elif (f(a) == 0):
        print" "
        print"The function is nul on : ", a
elif (f(b) == 0):
        print" "
        print"The function is nul on : ", b
else:
        print" "
        print "The function is nul on : ", Dichotomy(a, b)  

os.system("pause")
