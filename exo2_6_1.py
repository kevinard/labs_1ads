# 2.6.1
#
# Carré Magique
#
# Voir labs


def sommeCoefficients(l):
    somme = 0

    for i in l:
        for j in i:
            somme += j

    return somme


def ligneMagique(l, valeur, ligne):
    somme = 0

    for i in l[ligne-1]:
        somme += i

    return somme == valeur


def colonneMagique(l, valeur, colonne):
    somme = 0

    for i in l:
        somme += i[colonne-1]

    return somme == valeur


def diagonaleMagique(l, valeur, diagonale):
    somme = 0

    if diagonale == 1:
        current_index = 0
    else:
        current_index = -1

    for i in l:
        somme += i[current_index]

        if diagonale == 1:
            current_index += 1
        else:
            current_index -= 1

    return somme == valeur


def carreMagique(l):
    sommeCoeff = sommeCoefficients(l)

    for i in range(len(l)):
        if not ligneMagique(l, sommeCoeff//3, i) or not colonneMagique(l, sommeCoeff//3, i):
            return False

    if not diagonaleMagique(l, sommeCoeff//3, 1) or not diagonaleMagique(l, sommeCoeff//3, 2):
        return False

    return True

# ne s'exécute que si on exécute le fichier directement (cela évite d'exécuer ce code lorsqu'on fait un import de
# ce module (voir exo 2.6.2)
if __name__ == "__main__":
    maListe = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
    maListe2 = [[6, 7, 2], [2, 6, 9], [8, 3, 4]]
    print(sommeCoefficients(maListe))
    print(ligneMagique(maListe, 15, 2))
    print(ligneMagique(maListe2, 15, 2))
    print(colonneMagique(maListe, 15, 1))
    print(colonneMagique(maListe2, 15, 1))
    print(diagonaleMagique(maListe, 15, 1))
    print(diagonaleMagique(maListe, 15, 2))
    print(diagonaleMagique(maListe2, 15, 1))
    print(diagonaleMagique(maListe2, 15, 2))
    print(carreMagique(maListe))
    print(carreMagique(maListe2))
