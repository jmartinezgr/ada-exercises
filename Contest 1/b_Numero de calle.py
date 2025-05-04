def sum_sq_formula(k):
    return (k * (k + 1) * (2 * k + 1)) // 6


def sum_sq_upto(k1, k2):
    return sum_sq_formula(k2) - sum_sq_formula(k1)


def valores_validos(N):
    resultados = 0
    total = sum_sq_formula(N)
    for n in range(3, N):
        s1 = sum_sq_formula(n - 1)
        sn = sum_sq_formula(n)
        s2 = total - sn
        if s1 > s2:
            break
        if s1 != 0 and s2 % s1 == 0:
            resultados += 1
    return resultados


while True:
    N = int(input())
    if N == 0:
        break
    print(valores_validos(N))
