# 3.1.2
#
# Suite de Syracuse
#
# Ecrire une fonction récursive permettant de calculer le n ième terme de la suite de Syracuse.


def syracuse(n, a):
    if type(a) is not int or a < 0:
        print("Erreur : a doit être un entier positif.")
        return -1

    if n == 0:
        return a
    else:
        precedent = syracuse(n-1, a)

        if precedent % 2 == 0:
            return precedent // 2
        else:
            return 3*precedent+1


print(syracuse(21, 15))

