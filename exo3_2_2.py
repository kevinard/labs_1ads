# 3.2.2
#
# Tours de Hanoï
#
# Voir labs


def deplacer(n, origine, destination):
    if n == 1:
        print(origine, "->", destination)
    else:
        deplacer(n-1, origine, 6-(origine+destination))
        deplacer(1, origine, destination)
        deplacer(n-1, 6-(origine+destination), destination)

deplacer(3, 1, 3)
