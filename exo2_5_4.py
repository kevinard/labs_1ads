# 2.5.4
#
# Calcul de l’indice du minimum d’une liste
#
# Ecrire une fonction calculant l’indice du plus petit élément d’une liste de données numériques.


def getMinimumIndex(l):
    minimum_index = None

    for i in range(len(l)):
        if minimum_index is None or l[i] <= l[minimum_index]:
            minimum_index = i

    return minimum_index

maListe = [1, 2, 3, 4, 5]
print(getMinimumIndex(maListe))

maListe = [234, 235, 678, 6874, 51]
print(getMinimumIndex(maListe))

