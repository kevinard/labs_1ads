# 2.1.7
#
# Multiplications par additions successives
#
# Ecrire un programme effectuant la multiplication de deux entiers naturels en utilisant uniquement l’opération d’addition.

x, y = None, None

while type(x) is not int:
    x = eval(input("Entrez le premier nombre : "))

while type(y) is not int:
    y = eval(input("Entrez le second nombre : "))

produit = 0

for i in range(1, x+1):
    produit += y

print(str(x)+"*"+str(y), "=", produit)
