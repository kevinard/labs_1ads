# 3.3.1
#
# Tri à bulles
#
# Ecrire une procédure réalisant le tri à bulles d’une liste de données numériques (voir le module de cours
# pour l’explication du fonctionnement de cet algorithme).


def tri_bulles(l):
    permutation = True
    while permutation:
        permutation = False
        for i in range(0, len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                permutation = True

maListe = [4, 7, 1, 9, 2, 5, 3, 1, 10]
tri_bulles(maListe)
print(maListe)
