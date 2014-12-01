# 3.1.4
#
# Recherche d’un élément dans une liste (bis)
#
# Ecrire une fonction récursive indiquant si un élément est présent ou non dans une liste. Cette fonction retournera
# un booléen. On fera un test sur le premier élément, puis si besoin est l’appel récursif se fera sur la « fin » de
# la liste.


def recherche(l, x):
    if len(l) == 0:
        return False

    if l[0] == x:
        return True
    else:
        return recherche(l[1:], x)

maListe = [2, 5, 8, 1, 9]
print(recherche(maListe, 1))
print(recherche(maListe, 7))
