# Title : Input Box
# Readme : this program creates a box to input data with a button to close it

# importing useful packages
from Tkinter import *
from math import *

def evaluer(event):
	chaine.configure(text="whatever"+str(eval(entree.get())))

# main block
fen1=Tk()
entree=Entry(fen1)
entree.bind("<Return>",evaluer)
chaine=Label(fen1)
entree.pack()
chaine.pack()
text1=Label(fen1,text='The program will do... : ',fg='black',height=20,width=70)
text1.pack(side=TOP)
bou1=Button(fen1,text='Close',command=fen1.destroy)
bou1.pack(side=BOTTOM,padx=10,pady=10)
fen1.mainloop()

