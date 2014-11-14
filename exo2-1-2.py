# 2.1.2
#
# Savoir si trois entiers sont triés
#
# Ecrire un programme faisant saisir trois entiers x, y, z à l’utilisateur, et lui indiquant si ces nombres sont dans
# l’ordre croissant (x <= y <= z).

x, y, z = None, None, None

while type(x) is not int:
    x = eval(input("Entrez le premier nombre : "))

while type(y) is not int:
    y = eval(input("Entrez le second nombre : "))

while type(z) is not int:
    z = eval(input("Entrez le troisième nombre : "))

if x <= y <= z:
    print("Les nombres sont dans l'ordre croissant.")
else:
    print("Les nombres ne sont pas dans l'ordre croissant.")
