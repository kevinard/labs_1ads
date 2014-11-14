# 2.1.5
#
# Somme des premiers carrés
#
# Ecrire un programme calculant la somme des n premiers carrés d’entiers, où n est un entier naturel
# saisi par l’utilisateur.

n = None

while type(n) is not int:
    n = eval(input("Entrez un entier : "))

for i in range(n+1):
    print(str(i)+"**2 =", i**2)
