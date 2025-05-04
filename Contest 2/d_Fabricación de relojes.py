from math import gcd

for _ in range(int(input())):
    I, V, X = list(map(int, input().split()))

    divisorComun = gcd(gcd(I, V), X)
    tamanoMolde = (I + V + X) // divisorComun

    print(tamanoMolde)
