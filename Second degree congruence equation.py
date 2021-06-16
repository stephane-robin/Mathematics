# RESOLUTION OF THE EQUATION x^2+b x+c=0(mod n)
# Program written in Python 2.7
# This program solves the equation a x^2+b x+c=0(mod n) where the unknown is x

# This program is unfinished. It needs to add the package to read latex code

# PREAMBLE
print("- RESOLUTION OF THE EQUATION $a x**2+b x+c=0 $ - ")
print(" ")
print("This program solves the equation where the unknown is x")
print(" ")
a=input("Please enter the integer a : ")
a=int(a)
print(" ")
b=input("Please enter the integer b : ")
b=int(b)
print(" ")
c=input("Please enter the integer c : ")
c=int(c)
print(" ")
n=input("please enter the integer n : ")
n=int(n)
print(" ")
print(" ")
# ==================================================================

# FIND THE SOLUTIONS
print("Modulo ",n," the solutions are : ")
i=0
for k in range(0,n):
    x=(a*(k**2)+b*k+c)%n
    if (x==0):
        print(k)
        i=i+1
if (i==0):
    print("none")



# ==================================================================


