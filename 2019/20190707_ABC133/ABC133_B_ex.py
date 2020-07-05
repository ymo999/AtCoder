def dist(a, b):
    v = 0
    for d in range(D):
        v += (a[d]-b[d])**2
    v = v ** 0.5
    return v


N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N-1):
    for j in range(i+1, N):
        if dist(X[i], X[j]).is_integer():
            ans += 1

print(ans)
