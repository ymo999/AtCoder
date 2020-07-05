X, N = map(int, input().split())
if N == 0:
    print(X)
    exit()
else:
    P = list(map(int, input().split()))

n_P = []

for i in range(1, 100):
    if i not in P:
        n_P.append(i)

n_P.append(0)
n_P.append(101)

n_P.sort()
INF = 10 ** 9
diff = INF
ans = INF

for p in n_P:
    if abs(X-p) < diff:
        diff = abs(X-p)
        ans = p

print(ans)
