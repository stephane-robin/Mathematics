from matplotlib import pyplot # Bibliothèque nécessaire pour tracer des graphes
from math import * # Bibliothèque nécessaire pour utiliser pi et la fonction sinus

L=1000
periode=50
longueurOnde=L/2.5
amplitude=100

for t in range(0,5*periode) :
    list_x = [] # Création d'une liste vide pour y stocker les abscisses des points
    list_y1 = [] # Création d'une liste vide pour y stocker les ordonnées des points de l'onde 1
    list_y2 = [] # Création d'une liste vide pour y stocker les ordonnées des points de l'onde 2
    list_y3 = [] # Création d'une liste vide pour y stocker les ordonnées des points des ondes superposées
    
    for point in range(0,L) :
        list_x.append(point)
        list_y1.append(amplitude*sin((2*pi*t/periode)-(2*pi*list_x[point]/longueurOnde)))
        list_y2.append(amplitude*sin((2*pi*t/periode)+(2*pi*list_x[point]/longueurOnde)))
        list_y3.append(amplitude*sin((2*pi*t/periode)-(2*pi*list_x[point]/longueurOnde))+amplitude*sin((2*pi*t/periode)+(2*pi*list_x[point]/longueurOnde))) 

    pyplot.clf() # Permet d'effacer le contenu du graphique
    pyplot.axis([0, L, -L/2, L/2]) # Fixe les valeurs minimales et maximales
    pyplot.xlabel("x (mm)") # Indique la grandeur et l'unité sur l'axe des abscisses
    pyplot.ylabel("y (mm)") # Indique la grandeur et l'unité sur l'axe des ordonnées
    pyplot.title("Simulation d'une onde stationnaire le long d'une corde") # Donne un titre à l'animation
    pyplot.plot(list_x, list_y1, c = 'blue', marker = ',') # courbe de l'onde 1
    pyplot.plot(list_x, list_y2, c = 'red', marker = ',') # courbe de l'onde 2
    pyplot.plot(list_x, list_y3, c = 'green', marker = ',') # courbe des ondes superposées
    pyplot.pause(0.001)
    
pyplot.show()
