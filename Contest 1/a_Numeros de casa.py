import math

n = int(input())
response = ""
for i in range(n):
    N = int(input())
    i = math.sqrt((N**2 + N) / 2)
    if i == int(i):
        response += f"{int(i)}\n"
    else:
        response += "NO\n"

print(response.strip())
