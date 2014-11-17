# 2.4.1
#
# Nombres parfaits
#
# Ecrire un programme affichant tous les nombres parfaits jusqu’à un entier n saisi par l’utilisateur. Pour rappel,
# un nombre est parfait s’il est égal à la somme de ses diviseurs stricts (c’est à dire excepté lui même).


def nombresParfaits():
    n = None

    while type(n) is not int:
        n = eval(input("Entrez un nombre : "))

    afficherNombresParfaitsJusqua(n)


def afficherNombresParfaitsJusqua(n):
    for i in range(0, n+1):
        if estParfait(i):
            print(i)


def estParfait(n):
    if sommeDesDiviseurs(n) == n:
        return True
    else:
        return False


def sommeDesDiviseurs(n):
    somme = 0

    for i in range(1, n):
        if estUnDiviseur(n, i):
            somme += i

    return somme


def estUnDiviseur(x, y):
    if x % y == 0:
        return True
    else:
        return False

nombresParfaits()
