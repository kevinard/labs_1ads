# 2.6.2
#
# Jeu du Morpion
#
# Voir labs


def afficherPlateau(l):
    for i in l:
        for j in i:
            if j == 0:
                symbole = '.'
            elif j == 1:
                symbole = 'x'
            else:
                symbole = 'o'

            print(symbole, ' ', end='')

        print("\n")


def cases_vides(l):
    for i in l:
        for j in i:
            if j == 0:
                return True

    return False


def ligne_morpion(l, valeur, ligne, joueur):
    somme = 0

    for i in l[ligne-1]:
        if i == joueur:
            somme += i

    return somme == valeur


def colonne_morpion(l, valeur, colonne, joueur):
    somme = 0

    for i in l:
        if i[colonne-1] == joueur:
            somme += i[colonne-1]

    return somme == valeur


def diagonale_morpion(l, valeur, diagonale, joueur):
    somme = 0

    if diagonale == 1:
        current_index = 0
    else:
        current_index = -1

    for i in l:
        if i[current_index] == joueur:
            somme += i[current_index]

        if diagonale == 1:
            current_index += 1
        else:
            current_index -= 1

    return somme == valeur


def jouer(l, joueur):
    x, y = None, None

    while type(x) is not int or type(y) is not int or l[x-1][y-1] != 0:
        x, y = eval(input("Entrez la ligne : ")), eval(input("Entrez la colonne : "))

    l[x-1][y-1] = joueur


def victoire(l, joueur):
    for i in range(len(l)):
        if ligne_morpion(l, 3*joueur, i+1, joueur):
            return True
        if colonne_morpion(l, 3*joueur, i+1, joueur):
            return True

    if diagonale_morpion(l, 3*joueur, 1, joueur) or diagonale_morpion(l, 3*joueur, 2, joueur):
        return True

    return False


def jeu_morpion():
    plateau = [[0]*3 for i in range(3)]

    afficherPlateau(plateau)
    joueur_courant = 1

    while cases_vides(plateau) and not victoire(plateau, 1) and not victoire(plateau, 2):
        jouer(plateau, joueur_courant)
        afficherPlateau(plateau)

        if joueur_courant == 1:
            joueur_courant = 2
        else:
            joueur_courant = 1

    if victoire(plateau, 1):
        print("Le joueur 1 a gagné !")
    elif victoire(plateau, 2):
        print("Le joueur 2 a gagné !")
    else:
        print("Match nul.")

jeu_morpion()
