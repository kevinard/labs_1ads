# 2.3.5
#
# Suite de Conway
#
# Ecrire une procédure affichant les n premiers termes de la suite de Conway. Cette procédure appellera une fonction
# qui à partir d’un terme de la suite calcule le suivant. On pourra, si on le souhaite, traiter les termes de la
# suite sous forme de chaînes de caractère plutôt que sous forme de nombres.


def conway_next(n):
    compte = 0
    caractere_courant = None
    next = ""

    for i in range(0, len(n)):
        if caractere_courant is None:
            caractere_courant = n[i]

        if n[i] != caractere_courant:
            next += str(compte)+caractere_courant
            compte = 1
            caractere_courant = n[i]
        else:
            compte += 1

        if i == len(n)-1:
            next += str(compte)+caractere_courant

    return next


def conway(n):
    if type(n) is not int or n < 1:
        print("Erreur : n doit être un entier positif.")

    print("Terme 1 = 1")

    if n > 1:
        precedent = "1"
        for i in range(2, n+1):
            precedent = conway_next(precedent)
            print("Terme", i, "=", precedent)

conway(7)
