import math

n, d = map(int, input().split())
watch = d * 2 + 1

ans = math.ceil(n / watch)
print(ans)
