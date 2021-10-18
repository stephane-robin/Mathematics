def division(a, b, n):
    q = a // b
    a = a % b
    resultat = str(q) + ","
    for i in range(n):
        a = 10 * a
        q = a // b
        a = a % b
        resultat = resultat + str(q)
    return resultat

print(division(7, 27, 100))
