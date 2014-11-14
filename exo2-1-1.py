# 2.1.1
#
# Calcul du montant d'une remise
#
# Un commerçant accorde une remise de 5 % pour tout achat d’un montant compris entre 100 et 500 € et 8 % au-delà.
# Écrire un programme de calcul du montant de la remise sur un achat donné.

montant = -1

while montant < 0:
    montant = eval(input("Quel est le montant de l'achat ? "))

remise = 0

if 100 <= montant <= 500:
    remise = 0.05
elif montant > 500:
    remise = 0.08

print("Remise de", str(remise*100)+"%")
print("Le montant après remise est : ", montant-(montant*remise))

