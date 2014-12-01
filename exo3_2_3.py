# 3.2.3
#
# Retour sur l’algorithme de Karatsuba
#
# Voir labs


def karatsuba(x, y):
    if x < 10 or y < 10:
        return x*y

    m = max([len(str(x)), len(str(y))])
    n = (m+1) // 2

    x, y = list(str(x)), list(str(y))

    b, d = [], []

    for i in range(0, n):
        b.append(x.pop())
        d.append(y.pop())

    b.reverse()
    d.reverse()

    a = int("".join(x))
    b = int("".join(b))
    c = int("".join(y))
    d = int("".join(d))

    u = karatsuba(a, c)
    v = karatsuba(a+b, c+d)
    w = karatsuba(b, d)

    return u*(10**(2*n))+(v-u-w)*(10**n)+w

print(karatsuba(12, 34))
print(karatsuba(1234, 321))
