import math


def contar_distribuciones(E):
    divisores = 0
    for i in range(1, int(math.sqrt(E)) + 1):
        if E % i == 0:
            divisores += 1  # i es divisor
            if i != E // i:
                divisores += 1  # E // i también lo es (si no es el mismo)
    return divisores


# Lectura de input
N = int(input())
for _ in range(N):
    E = int(input())
    print(contar_distribuciones(E))
