# 3.2.1
#
# Exponentiation rapide
#
# Voir labs


def exposant(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return exposant(x*x, n/2)
    else:
        return x*exposant(x*x, (n-1)/2)


print(exposant(3, 5))
print(exposant(4, 4))
print(exposant(7, 3))
print(exposant(8, 6))
