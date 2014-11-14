# 2.1.3
#
# Tri de trois réels
#
# Ecrire un programme faisant saisir trois nombres réels x, y, z à l’utilisateur et qui les trie par ordre croissant
# (à la fin du déroulement du programme x ≤ y ≤ z).

x, y, z = None, None, None

x = eval(input("Entrez le premier nombre : "))
y = eval(input("Entrez le second nombre : "))
z = eval(input("Entrez le troisième nombre : "))

if x > y:
    x, y = y, x

if y > z:
    y, z = z, y

if x > y:
    x, y = y, x

print(x,"<=",y,"<=",z)
