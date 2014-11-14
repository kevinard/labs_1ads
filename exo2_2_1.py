# 2.2.1
#
# De jolies étoiles !!!
#
# Voir labs

x = None

while type(x) is not int or x < 0:
    x = eval(input("Entrez un nombre : "))

for i in range(x, 0, -1):
    print(i*"*")
