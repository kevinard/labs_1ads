# 2.5.2
#
# Recherche d’un élément dans une liste
#
# Ecrire une fonction indiquant si un élément est présent ou non dans une liste. S’il est présent cette fonction
# retournera l’indice de la case où il se trouve pour la première fois, et s’il est absent elle retournera -1.


def recherche(l, x):
    for i in range(len(l)):
        if l[i] == x:
            return i

    return -1


maListe = [1, 2, 3, 4, 5]
print(recherche(maListe, 3))
print(recherche(maListe, 6))
