# 2.1.6
#
# Suite de nombres pairs
#
# Ecrire un programme affichant une suite de nombres pairs dans une plage déterminée par l’utilisateur.
# Ce dernier entre au clavier une borne basse, ainsi qu’une borne haute, et le programme affiche dans un
# ordre croissant les nombres pairs compris dans ce domaine, sans inclure les bornes.

x, y = None, None

while type(x) is not int:
    x = eval(input("Entrez la borne basse : "))

while type(y) is not int:
    y = eval(input("Entrez la borne haute : "))

if x%2 == 0:
    x += 1

for i in range(x+1, y, 2):
    print(i)
