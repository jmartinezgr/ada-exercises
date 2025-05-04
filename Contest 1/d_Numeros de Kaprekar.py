def is_kaprekar(n):
    squared = n * n
    str_squared = str(squared)

    for i in range(1, len(str_squared)):
        left_part = int(str_squared[:i])
        right_part = int(str_squared[i:])

        if right_part == 0:
            continue

        if left_part + right_part == n:
            return True
    return False


for _ in range(int(input())):
    n = int(input())
    print("KAP" if is_kaprekar(n) else "NO")
