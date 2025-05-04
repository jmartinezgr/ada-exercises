def suma_potencias_mod(N, p, k=49999):
    return sum(pow(i, p, k) for i in range(1, N + 1)) % k


n = int(input())

response = ""

for i in range(n):
    N, P = map(int, input().split())

    response += f"{suma_potencias_mod(N, P)}" + "\n"

print(response.strip())
