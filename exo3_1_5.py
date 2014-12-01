# 3.1.5
#
# Recherche d’un élément dans une liste (ter)
#
# Ecrire une fonction récursive indiquant si un élément est présent ou non dans une liste. S’il est présent cette
# fonction retournera l’indice de la case où il se trouve pour la première fois, et s’il est absent elle
# retournera -1. On fera un test sur le premier élément, puis si besoin est l’appel récursif se fera sur la « fin »
# de la liste.


def recherche(l, x, p=0):
    if len(l) == p:
        return -1

    if l[p] == x:
        return p
    else:
        return recherche(l, x, p+1)

maListe = [2, 5, 8, 1, 9]
print(recherche(maListe, 1))
print(recherche(maListe, 7))
