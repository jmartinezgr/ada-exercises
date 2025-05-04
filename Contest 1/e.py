def es_capicua(n):
    return str(n) == str(n)[::-1]


def invertir(n):
    return int(str(n)[::-1])


def procesar_numero(n):
    iteraciones = 0
    if es_capicua(n):
        return 0
    while n < 10**10:
        r = invertir(n)
        n += r
        iteraciones += 1
        if es_capicua(n):
            return iteraciones
    return "L"


while True:
    entrada = input()
    if entrada == "0":
        break
    n = int(entrada)
    print(procesar_numero(n))
