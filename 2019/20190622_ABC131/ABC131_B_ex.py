n, l = map(int, input().split())
taste = []
abs_v = []

for i in range(n):
    taste.append(l+i)
    abs_v.append(abs(l+i))

idx = abs_v.index(min(abs_v))
del taste[idx]

print(sum(taste))
