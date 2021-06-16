# LOI DES GRANDS NOMBRES
# Programme rédigé en Python 2.7
# Voici un exemple d'application de la loi des grands nombres
# On lance n fois un de à 6 faces.
# Les resultats affiches sont les pourcentages de tirages pour chaque face.
# Le premier resultat correspond à 10 lances, le deuxieme à 100 lances et le troisieme à 10000 lances.
# On remarque qu'avec un grand nombre de lances, le resultat se rapproche de la probabilite de 16.66%

# PREAMBULE
print("-- LOI DES GRANDS NOMBRES --")
print(" ")
print("Voici un exemple d'application de la loi des grands nombres")
print("On lance n fois un de à 6 faces.")
print("Les resultats affiches sont les pourcentages de tirages pour chaque face.")
print("Le premier resultat correspond à 10 lances, le deuxième à 100 lances et le troisieme à 100000 lances.")
print("On remarque qu'avec un grand nombre de lances, le resultat se rapproche de la probabilite de 16.66%")
print(" ")
# ==================================================================

# 10 LANCES
n=10
x1,x2,x3,x4,x5,x6=0.,0.,0.,0.,0.,0.
for k in range(1,n+1):
    x=randint(1,7)
    if x==1:
        x1=x1+1
    if x==2:
        x2=x2+1
    if x==3:
        x3=x3+1
    if x==4:
        x4=x4+1
    if x==5:
        x5=x5+1
    if x==6:
        x6=x6+1
x1=100*x1/n
x2=100*x2/n
x3=100*x3/n
x4=100*x4/n
x5=100*x5/n
x6=100*x6/n
print("Les resultats obtenus pour ",n," lances sont : ")
print("1: ",round(x1,2),"%, "," 2: ",round(x2,2),"%, "," 3: ",round(x3,2),"%, "," 4: ",round(x4,2),"%, "," 5: ",round(x5,2),"%, "," 6: ",round(x6,2),"%, ")
print(" ")
# ======================================================================

# 100 LANCES
n=100
x1,x2,x3,x4,x5,x6=0.,0.,0.,0.,0.,0.
for k in range(1,n+1):
    x=randint(1,7)
    if x==1:
        x1=x1+1
    if x==2:
        x2=x2+1
    if x==3:
        x3=x3+1
    if x==4:
        x4=x4+1
    if x==5:
        x5=x5+1
    if x==6:
        x6=x6+1
x1=100*x1/n
x2=100*x2/n
x3=100*x3/n
x4=100*x4/n
x5=100*x5/n
x6=100*x6/n
print("Les resultats obtenus pour ",n," lances sont : ")
print("1: ",round(x1,2),"%, "," 2: ",round(x2,2),"%, "," 3: ",round(x3,2),"%, "," 4: ",round(x4,2),"%, "," 5: ",round(x5,2),"%, "," 6: ",round(x6,2),"%, ")
print(" ")
# ====================================================================

n=1000
x1,x2,x3,x4,x5,x6=0.,0.,0.,0.,0.,0.
for k in range(1,n+1):
    x=randint(1,7)
    if x==1:
        x1=x1+1
    if x==2:
        x2=x2+1
    if x==3:
        x3=x3+1
    if x==4:
        x4=x4+1
    if x==5:
        x5=x5+1
    if x==6:
        x6=x6+1
x1=100*x1/n
x2=100*x2/n
x3=100*x3/n
x4=100*x4/n
x5=100*x5/n
x6=100*x6/n
print("Les resultats obtenus pour ",n," lances sont : ")
print("1: ",round(x1,2),"%, "," 2: ",round(x2,2),"%, "," 3: ",round(x3,2),"%, "," 4: ",round(x4,2),"%, "," 5: ",round(x5,2),"%, "," 6: ",round(x6,2),"%, ")
print(" ")
# =====================================================================

# 1000000 LANCES
n=1000000
x1,x2,x3,x4,x5,x6=0.,0.,0.,0.,0.,0.
for k in range(1,n+1):
    x=randint(1,7)
    if x==1:
        x1=x1+1
    if x==2:
        x2=x2+1
    if x==3:
        x3=x3+1
    if x==4:
        x4=x4+1
    if x==5:
        x5=x5+1
    if x==6:
        x6=x6+1
x1=100*x1/n
x2=100*x2/n
x3=100*x3/n
x4=100*x4/n
x5=100*x5/n
x6=100*x6/n
print("Les resultats obtenus pour ",n," lances sont :")
print("1: ",round(x1,2),"%, "," 2: ",round(x2,2),"%, "," 3: ",round(x3,2),"%, "," 4: ",round(x4,2),"%, "," 5: ",round(x5,2),"%, "," 6: ",round(x6,2),"%, ")
print(" ")
# =====================================================================

