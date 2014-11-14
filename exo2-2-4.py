# 2.2.4
#
# Palindrome
#
# Ecrire un programme qui détermine si une chaine de caractère donnée est un palindrome.
# Rappelons qu’un palindrome est un mot qui se lit « dans les deux sens », comme par exemple « laval ».

string = str(input("Entrez une chaine de caractères : "))

palindrome = True

for i in range(len(string)):
    if string[i] != string[-i-1]:
        palindrome = False
        break

if palindrome:
    print(string, "est un palindrome.")
else:
    print(string, "n'est pas un palindrome.")
