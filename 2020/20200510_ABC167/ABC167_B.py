A, B, C, K = map(int, input().split())
ans = 0

if A > 0 and K > 0:
    ans += min(A, K) * 1
    K -= min(A, K)
if B > 0:
    K -= min(B, K)
if C > 0:
    ans += min(C, K) * (-1)
    K -= min(C, K)

print(ans)
