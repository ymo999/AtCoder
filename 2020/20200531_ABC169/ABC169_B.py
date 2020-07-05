N = int(input())
A = list(map(int, input().split()))
INF = 10 ** 18

if 0 in A:
    print(0)
    exit()

A.sort(reverse=True)
ans = A[0]

for i in range(1, N):
    if A[i] > INF:
        print(-1)
        exit()
    if A[i] == 1:
        break
    ans = ans * A[i]
    if ans > INF:
        print(-1)
        exit()

print(ans)
