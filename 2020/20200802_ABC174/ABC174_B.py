N, D = map(int, input().split())

XY = []

for _ in range(N):
    XY.append(list(map(int, input().split())))

ans = 0

for p, q in XY:
    if (p**2+q**2)**0.5 <= D:
        ans += 1

print(ans)
