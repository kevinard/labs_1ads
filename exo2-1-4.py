# 2.1.4
#
# Signe d’un produit
#
# Ecrire un programme qui calcule le signe du produit de deux nombres réels sans calculer la valeur de ce produit.
# Par signe, on entend positif, négatif ou nul.

x, y = eval(input("Entrez le premier nombre : ")), eval(input("Entrez le second nombre : "))

# on pose 1 pour un signe positif et -1 pour un signe négatif et 0 pour un nombre nul
signe_x = 0
signe_y = 0

if x < 0:
    signe_x = -1
elif x > 0:
    signe_x = 1

if y < 0:
    signe_y = -1
elif y > 0:
    signe_y = 1

if signe_x == 0 or signe_y == 0:
    print("Le produit est nul.")
elif (signe_x == 1 and signe_y == 1) or (signe_x == -1 and signe_y == -1):
    print("Le produit est positif.")
else:
    print("Le produit est négatif.")
