N = int(input())
A = list(map(int, input().split()))
ans = 0
pre = 0

for a in A:
    if pre > a:
        ans += pre - a
        a = pre
    pre = a

print(ans)
