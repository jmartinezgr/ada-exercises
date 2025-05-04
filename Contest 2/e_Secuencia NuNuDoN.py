def contar_divisores(n):
    divisores = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisores += 1
            if i != n // i:
                divisores += 1
    return divisores


MAX_N = 100000
sec = [1]

while sec[-1] <= MAX_N:
    last = sec[-1]
    divisores = contar_divisores(last)
    sec.append(last + divisores)

sec = [x for x in sec if x <= MAX_N]

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    resultado = sum(1 for x in sec if A <= x <= B)
    print(resultado)
