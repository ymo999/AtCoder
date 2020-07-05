import math

k = int(input())
s = 0
for i in range(1, k + 1):
    for j in range(1, k + 1):
        s1 = math.gcd(i, j)
        for k in range(1, k + 1):
            s += math.gcd(k, s1)
print(s)
