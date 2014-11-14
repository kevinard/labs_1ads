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
        return fibonacci(n-1)+fibonacci(n-2)
    else:
        print("Erreur : n doit être >= 0")
        return -1

print("n=0 =>", fibonacci(0))
print("n=1 =>", fibonacci(1))
print("n=2 =>", fibonacci(2))
print("n=3 =>", fibonacci(3))
print("n=-2 =>", fibonacci(-2))
print("n=9 =>", fibonacci(9))
