# 2.3.2
#
# Suite de Syracuse
#
# Ecrire une procédure affichant les n premiers termes de la suite de Syracuse de base a.


def syracuse(n, a):
    if type(a) is not int or a < 0:
        print("Erreur : a doit être un entier positif.")

    print(a, end=" ")

    precedent = a

    for i in range(1, n):
        if precedent%2 == 0:
            precedent //= 2
        else:
            precedent = 3*precedent+1

        print(precedent, end=" ")

    print("\n")


syracuse(21, 15)
