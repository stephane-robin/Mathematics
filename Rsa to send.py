# RSA MESSAGE TO SEND
# Program written in Python 2.7
# This program transforms a letter into a Rsa code
# code parameters : p=23, q=17, e=47, d=15

# Importing useful packages
import os
import math as m

# Introduction
print "- RSA MESSAGE TO SEND -"
print" "
print"This program transforms a letter into a RSA code"
print " "

# MAIN COMMAND
x=input("Please enter the letter you want to turn into code (use the symbols ' ' around this letter) : ")
print(ord(x)^47)%391

os.system("pause")
