# SIEVE OF ERATOSTHENES
# program written in Python 2.7 , finds prime numbers smaller than an integer

# IMPORTING USEFUL PACKAGES
import os

# MAIN DIRECTORY
print("- Sieve of Erastothenes -")
print(" ")

# input the border
N=input("Please enter the integer under which we'll find prime numbers : ")
N=int(N)

def Eratosthene(x):
        prime_list=range(3,x,2)
	
        for i in range(3,x,2):
        	prime_list.append(i)
		
        for i in prime_list:
        	for n in prime_list:
        		if n%i==0 and i!=n:
        			prime_list.remove(n)
	
        return prime_list
       

print(Eratosthene(N))

os.system("pause")
