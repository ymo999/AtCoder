import itertools

N = int(input())
L = list(map(int, input().split()))

if N < 3:
    print(0)
    exit()

ans = 0

for bars in itertools.combinations(L, 3):
    if max(bars) >= sum(bars) - max(bars):
        continue
    if bars[0] == bars[1]:
        continue
    if bars[1] == bars[2]:
        continue
    if bars[0] == bars[2]:
        continue
    ans += 1

print(ans)
