# 2.3.3
#
# Distance de Hamming
#
# La distance de Hamming entre deux chaînes de caractères supposées de même longueur est égale au nombre de caractères
# à la même position qui diffèrent.
# Par exemple la distance de Hamming entre “papa“ et “papi“ est égale à 1. La distance entre “supinfo“ et “lutines“
# est égale à 4.
# Ecrire une fonction calculant la distance de Hamming de deux chaînes de caractères non vides que
# l’on sait de même longueur.


def hamming(a, b):
    if len(a) == 0 or len(b) == 0 or len(a) != len(b):
        print("Erreur : les 2 chaines doivent être de même longueur.")
        return -1

    distance = 0

    for i in range(0, len(a)):
        if a[i] != b[i]:
            distance += 1

    return distance


print("Distance de Hamming entre \"papa\" et \"papi\" :", hamming("papa", "papi"))
print("Distance de Hamming entre \"supinfo\" et \"lutines\" :", hamming("supinfo", "lutines"))
