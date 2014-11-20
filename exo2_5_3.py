# 2.4
#
# CALCUL DU MINIMUM D’UNE LISTE
#
# Ecrire une fonction calculant le plus petit élément d’une liste de données numériques.


def getMinimum(l):
    minimum = None

    for i in l:
        if minimum is None or i <= minimum:
            minimum = i

    return minimum

maListe = [1, 2, 3, 4, 5]
print(getMinimum(maListe))

maListe = [234, 235, 678, 6874, 51]
print(getMinimum(maListe))
