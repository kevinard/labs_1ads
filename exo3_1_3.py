# 3.1.3
#
# Somme des premiers cubes
#
# Ecrire une fonction récursive calculant la somme des n premiers cubes d’entiers.


def somme_cube(n):
    if n == 1:
        return 1
    else:
        return n**3 + somme_cube(n-1)


print(somme_cube(2))
print(somme_cube(3))
print(somme_cube(4))
print(somme_cube(8))
