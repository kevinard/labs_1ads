# 2.3.4
#
# Anagrammes
#
# Ecrire une fonction déterminant si deux mots donnés sont des anagrammes. Rappelons que des anagrammes sont des mots
# ayant exactement les mêmes lettres, comme par exemple « logarithme » et « algorithme ». On se servira librement
# des opérations connues sur les chaînes de caractères.


def anagrammes(a, b):
    if len(a) != len(b):
        return False

    reponse = True

    for i in range(0, len(a)):
        if not (a[i] in b):
            reponse = False
            break

        if a.count(a[i]) != b.count(a[i]):
            reponse = False
            break

    return reponse


if anagrammes("logarithme", "algorithme"):
    print("\"logarithme\" et \"algorithme\" sont des anagrammes")
else:
    print("\"logarithme\" et \"algorithme\" ne sont pas des anagrammes")


if anagrammes("supinfo", "lutines"):
    print("\"supinfo\" et \"lutines\" sont des anagrammes")
else:
    print("\"supinfo\" et \"lutines\" ne sont pas des anagrammes")
