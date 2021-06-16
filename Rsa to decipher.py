# RSA MESSAGE TO DECIPHER
# Program written in Python 2.7
# This program transforms a code into a letter
# code parameters : p=23, q=17, e=47, d=15

# Importing useful packages
import os
import math as m

# Introduction
print"- RSA MESSAGE TO DECIPHER -"
print " "
print "This program transforms a code into a letter"
print " "

# MAIN COMMAND
x=input("Please enter the code you want to decipher : ")
print chr((x^15)%391)

os.system("pause")
