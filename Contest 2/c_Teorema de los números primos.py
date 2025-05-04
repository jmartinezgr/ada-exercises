from math import log


def generarprimos(N):
    p = [True] * (N + 1)
    p[0] = p[1] = False
    for i in range(2, int(N**0.5) + 1):
        if p[i]:
            for j in range(i * i, N + 1, i):
                p[j] = False
    pi = [0] * (N + 1)
    contador = 0
    for i in range(2, N + 1):
        if p[i]:
            contador += 1
        pi[i] = contador
    return pi


cases = int(input())

N = [int(input()) for _ in range(cases)]

primos = generarprimos(max(N))

for n in N:
    print(int(round(primos[n] - (n / log(n)), 0)))
