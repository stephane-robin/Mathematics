3# INTEGRAL CALCULUS
# Program written in Python 3.3
# This program calculates the value of an integral as an approximation of the surface under the curve of the function
# Changing the definition of the function in the command line is necessary before running the program

# INTRODUCTION
print ("- INTEGRAL CALCULUS -")
print (" ")
print ("This program calculates the value of an intergal as an approximation of the surface under the curve of the function")
print (" ")
a=input("Please enter the value of the lower boundary :")
a=float(a)
b=input("Please enter the value of the higher boundary :")
b=float(b)
# ===============================================================

# DEFINE THE FUNCTION TO STUDY
def f(x):
    return x**2
# ====================================================================

# PROCESS THE VALUE OF THE INTEGRAL
I1,I2=0.,0.
for k in range(0,10000):
    I1=f(a+k*(b-a)/10000)+I1
I1=I1*(b-a)/10000

for k in range(1,10001):
    I2=f(a+k*(b-a)/10000)+I2
I2=I2*(b-a)/10000

print((I1+I2)/2)


