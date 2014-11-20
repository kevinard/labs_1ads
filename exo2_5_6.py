# 2.5.6
#
# Problème du drapeau hollandais, version simple
#
# Voir labs


def drapeau_hollandais(l):
    for i in range(len(l)):
        if l[i] == 2:
            l.pop(i)
            l.append(2)

    for i in range(len(l)):
        if l[i] == 3:
            l.pop(i)
            l.append(3)

    return l

maListe = [3, 2, 1, 2, 3, 1, 1, 3, 1]
print(drapeau_hollandais(maListe))
