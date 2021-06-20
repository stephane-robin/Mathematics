# GREATEST COMMON DIVIDER BY EUCLIDE ALGORITHM
# program written in python 2.7 , finds the gcd of 2 integers

# IMPORTING USEFUL PACKAGES
import os

# MAIN DIRECTORY
print ("- Greatest Common Divider by Euclide algorithm -")
print (" ")

# input of the 2 integers 
a = int(input("Please enter the first integer : "))  
b = int(input("Please enter the second integer : "))

def Euclide(x, y):
	r = x % y
	if r == 0:
		return y
	else:
		return Euclide(y, r)

if (Euclide(a, b) == 1):
	print (a," and ",b," are prime numbers")
else:
	print ("The greatest common divider of ", a, " and ", b, " is : ", Euclide(a, b))

# os.system("pause")
