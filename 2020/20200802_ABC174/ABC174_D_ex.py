N = int(input())
C = list(map(str, input()))

ans = 0

for i in range(N-1):
    if C[i] == 'W' and C[i+1] == 'R':
        tmp = C[i]
        C[i] = C[i+1]
        C[i+1] = tmp
        ans += 1

if C[N-2] == 'W' and C[N-1] == 'R':
    C[N-1] == 'W'
    ans += 1

print(ans)
