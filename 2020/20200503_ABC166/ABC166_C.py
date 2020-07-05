N, M = map(int, input().split())
H = list(map(int, input().split()))
result = [0] * N
route = [0] * N

for _ in range(M):
    A, B = map(int, input().split())
    route[A-1] = 1
    route[B-1] = 1
    if H[A-1] > H[B-1]:
        if result[A-1] != -1:
            result[A-1] = 1
        result[B-1] = -1
    elif H[A-1] < H[B-1]:
        result[A-1] = -1
        if result[B-1] != -1:
            result[B-1] = 1
    else:
        result[A-1] = -1
        result[B-1] = -1

print(result.count(1) + route.count(0))
