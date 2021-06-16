# SERIES CALCULUS
# Program written in Python 2.7
# This program gives the umpteenth term of a series

# Importing useful packages
import math
import os

# Introduction
print "SERIES CALCULUS"
print " "
print "This program gives the umpteenth term of a series"
print " "

# Defining the necessary terms
u=input ("Please enter the 1st term of the series : ")
u=float(u)
print " "
n=input("Please enter the term n of the series that you want to calculate : " )

# Defining the function
def suite(u):
    return u+1/u

# MAIN DIRECTORY
for k in range(1, n+1):
    u=suite(u)
print u

os.system("pause")
