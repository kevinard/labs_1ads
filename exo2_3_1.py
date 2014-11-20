# 2.3.1
#
# Suite de Fibonacci
#
# Ecrire une fonction calculant le n ième terme de la suite de Fibonacci.

# 0 1 1 2 3 5


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        precedent1 = 0
        precedent2 = 1
        terme = 0

        for i in range(2, n+1):
            terme = precedent1+precedent2
            precedent1 = precedent2
            precedent2 = terme

        return terme
    else:
        print("Erreur : n doit être >= 0")
        return -1


def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)
    else:
        print("Erreur : n doit être >= 0")
        return -1

print("n=0 =>", fibonacci(0))
print("n=1 =>", fibonacci(1))
print("n=2 =>", fibonacci(2))
print("n=3 =>", fibonacci(3))
print("n=-2 =>", fibonacci(-2))
print("n=9 =>", fibonacci(9))
