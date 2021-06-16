# RSA METHOD
# Program written in Python 3.3

# Importing useful packages
import os
from math import *
from numpy import *


# HEADER
print ("---RAS METHOD---")
print (" ")
print ("This program encodes a sentence and deciphers a code."
print (" ")
print ("If you want to encode a sentence, please type 1")
bouton=input ("If you want to decipher a code, please type 2")

# BODY
if bouton="1":
	phrase=input ("Please write the sentence you'd like to encode : ")
	for i in phrase: # select into the sentence and change each letter into a set of numbers
		if i=" ":
			print (" ")
		else print(ord(i)^47)%391
	
if bouton="2":
	code=input ("Please write the code you'd like to decipher. Don't forget to respect the spaces : ")
	c="0"
	for i in code:
		while i != " ":
			c.append(i)
			print chr((c^15)%391)
		else print (" ")
	
else print("Sorry but you entered an invalid answer.")

os.system("pause")

