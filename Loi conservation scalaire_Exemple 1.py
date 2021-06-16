# Loi conservation scalaire
# This program draws the classic solution for a loi de conservation scalaire in the 1st exemple of the lesson
# We take u_0=e^{-x^2}

# Importing useful packages
from matplotlib import pyplot as plt
import numpy as np

# Defining u_0
def u_0(y):
    return np.exp(-y**2)

# Drawing u(t,x) depending on t
t=0
while t<1:
    # Graph_1
    # Frame
    plt.figure(1)
    plt.xlabel("x(t)")
    plt.ylabel("u(t,x)")
    plt.grid(True)
    plt.xlim(-3,3)
    plt.ylim(-3,3)
    plt.title("u(t,x)")
    # X axis
    Xabs=np.linspace(-3,3,100)
    Xord=np.zeros(100)
    # Y axis
    Yabs=np.zeros(100)
    Yord=np.linspace(-3,3,100)
    plt.plot(Xabs,Xord,'k',Yabs,Yord,'k',linewidth=1)
    # Function
    x=np.linspace(-3,3,100)
    u=u_0(x/(x+(1-x)*np.exp(t)))
    plt.plot(x,u,'b',linewidth=2)
    t=t+0.1
    plt.show()



