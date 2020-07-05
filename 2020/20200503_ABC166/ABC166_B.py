N, K = map(int, input().split())
result = [0] * N

for k in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        result[a-1] = 1
    A.clear()

print(result.count(0))
