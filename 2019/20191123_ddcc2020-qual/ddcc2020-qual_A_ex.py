X, Y = map(int, input().split())
award = [300000, 200000, 100000]
ans = 0

if X <= 3:
    ans += award[X-1]

if Y <= 3:
    ans += award[Y-1]

if X == 1 and Y == 1:
    ans += 400000

print(ans)
