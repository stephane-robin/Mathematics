# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 10:31:08 2014

@author: stef
"""
# INITIAL ITERATIONS ===============================================



n=10

# DRAWING OMEGA ===================================================

def t(i):
    return 2*pi*i/100

def xOmegat(i):
    global t    
    return cos(t(i))

def yOmegat(i):
    global t    
    return sin(t(i))

for i in range(0,101):
    print(xOmegat(i))
    print(yOmegat(i))
    plot([xOmegat(i),yOmegat(i)],[xOmegat(i+1),yOmegat(i+1)],'r',linewidth=2)


# DRAWING DISCREET ================================================

def th(i):
    global n    
    return 2*pi*i/n

for i in range(0,11):
    plot(xOmega(th),yOmega(th),'k',linewidth=2)
    


