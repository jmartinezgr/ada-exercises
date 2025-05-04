import math
from functools import reduce


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_multiple(numbers):
    return reduce(lcm, numbers)


N = int(input())
for _ in range(N):
    periods = list(map(int, input().split()))
    print(lcm_multiple(periods))
