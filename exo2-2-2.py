# 2.2.2
#
# Encore de jolies étoiles !!!
#
# Voir labs

x = None

while type(x) is not int or x < 0:
    x = eval(input("Entrez un nombre : "))

max_char = x*2-1

for i in range(1, x+1):
    nb_star = i*2-1
    nb_space = (max_char-nb_star)//2
    print(nb_space*" ", nb_star*"*", nb_space*" ", sep="")
