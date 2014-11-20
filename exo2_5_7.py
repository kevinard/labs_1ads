# 2.5.7
#
# Problème du drapeau hollandais, version complexe
#
# Voir labs


def drapeau_hollandais(l):
    offset = 0
    for i in range(len(l)):
        print(l)
        if l[i-offset] == 1:
            l = [l[i-offset]] + l[:i-offset] + l[i-offset+1:]
        elif l[i-offset] == 3:
            l.pop(i-offset)
            l.append(3)
            offset += 1

    return l

maListe = [3, 2, 1, 2, 3, 1, 1, 3, 1]
print(drapeau_hollandais(maListe))
