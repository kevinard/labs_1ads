# 2.2.3
#
# Des tables de multiplication « exotiques »
#
# Voir labs

x = None

while type(x) is not int or x < 0:
    x = eval(input("Entrez un nombre : "))

for i in range(1, x+1):
    string = i*"1"
    number = int(string)
    print(string, "*", string, "=", number*number)

print("\n")

for i in range(1, x+1):
    string = ""
    for j in range(1, i+1):
        string += str(j)

    number = int(string)
    print(x, "*", string, "=", x*number)

print("\n")

for i in range(1, x+1):
    string = ""
    for j in range(1, i+1):
        string += str(j)

    number = int(string)
    print(x-1, "*", string, "+", str(i), "=", (x-1)*number+i)

print("\n")

for i in range(1, x+1):
    if x-i-1 < 0:
        break

    string = ""
    for j in range(x, x-i, -1):
        string += str(j)

    number = int(string)
    print(x, "*", string, "+", str(x-i-1), "=", x*number+(x-i-1))
