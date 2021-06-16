# Title : Babylon algorithm
# To read : this program gives the nroot of a number a providing this number is not too close to 0. It uses the Newton's method for a particular polynomial function.
# # warning : this method is very unstable and it is necessaty to choose an initial value close to the result which can't be too close to 0. It is hence necessary to check every result.
# program written in python 2.7

# importing useful packages
import os
import numpy as np
import math
from Tkinter import *

# Introduction window
fen=Tk()
fen.title("Babylon algorithm")
fen.geometry("500x300")

t=Text(fen,width=54,height=10,bg='grey',fg='black',font='Arial 12')
t.insert(END,"This program gives the nroot of a number a providing this number is not too close to 0. It uses the Newton's method for a particular polynomial function. The algorithm is hence very unstable and it is necessary to choose an initial value close to the result. It is also necessary to check every result.")
t.pack(side=TOP)

bou=Button(fen,text='Close',fg='black',font='Arial 10',bg='grey',command=fen.destroy)
bou.pack(side=BOTTOM,padx=10,pady=10)
fen.mainloop()

print "- Babylon algorithm -"
print "  "

# defining useful variables
a=input("Please enter the number a : ")
n=input("Please enter the nroot number n : ")
m=input("Please enter the number of iterations : ")
k=0
x=float(a)

# defining the sequence from Newton's method
while k<m:
	x=x*(1+(a/(x**2)-1)/n)
	k=k+1	

# showing the result
print n,"root of ",a," is : ",x

os.system("pause")
