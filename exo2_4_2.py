# 2.4.2
#
# Jeu des allumettes
#
# Voir labs

import random


def jeu_allumettes():
    nb_allumettes = None

    while type(nb_allumettes) is not int or nb_allumettes < 1 or nb_allumettes % 2 == 0:
        nb_allumettes = eval(input("Saississez un nombre impair d'allumettes : "))

    joueur_courant = None

    while type(joueur_courant) is not int or (joueur_courant != 1 and joueur_courant != 2):
        joueur_courant = eval(input("Voulez-vous commencer (1) ou que l'ordinateur commence (2) ? "))

    while nb_allumettes > 0:
        print("Il reste", nb_allumettes, "allumettes")
        joueur_courant, nb_allumettes = jouer(joueur_courant, nb_allumettes)

    if joueur_courant == 1:
        print("Le joueur a gagné.")
    else:
        print("L'ordinateur a gagné.")


def jouer(joueur_courant, nb_allumettes):
    allumettes = 0

    if joueur_courant == 1:
        while type(allumettes) is not int or allumettes < 1 or allumettes > 3:
            allumettes = eval(input("Combien prenez-vous d'allumettes (entre 1 et 3) ? "))

        joueur_courant = 2
    else:
        allumettes = choix_ordinateur()
        print("L'ordi a pris", allumettes, "allumettes.")
        joueur_courant = 1

    return joueur_courant, nb_allumettes-allumettes


def choix_ordinateur():
    return random.randint(1, 3)


def choix_ordinateur_ia(nb_allumettes):
    pass

jeu_allumettes()
