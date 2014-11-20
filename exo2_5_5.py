# 2.5.5
#
# Inversion d’une liste
#
# Ecrire une procédure réalisant l’inversion d’une liste de données numériques. Par exemple 4 2 3 7 8 devient 8 7 3 2 4.
# On n’utilisera pas d’autre liste que celle donnée.


def inverse(l):
    for i in range(len(l)//2):
        l[i], l[-(i+1)] = l[-(i+1)], l[i]

    return l

maListe = [1, 2, 3, 4, 5]
print(inverse(maListe))

maListe = [234, 235, 678, 6874, 51]
print(inverse(maListe))

maListe = [234, 235, 678, 6874]
print(inverse(maListe))
