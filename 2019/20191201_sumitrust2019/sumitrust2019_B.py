import math

n = int(input())
x = math.ceil(n / 1.08)
nx = math.floor(x * 1.08)

if n == nx:
    print(x)
else:
    print(':(')
