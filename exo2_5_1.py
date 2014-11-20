# 2.5.1
#
# Nombre d’occurrence d’un élément dans une liste
#
# Ecrire une fonction calculant le nombre d’occurrences d’un élément dans une liste.


def compteOccurrence(l, x):
    compte = 0

    for i in l:
        if l[i] == x:
            compte += 1

    return compte

maListe = [1, 2, 3, 4, 5, 3]
print(compteOccurrence(maListe, 2))
print(compteOccurrence(maListe, 3))
