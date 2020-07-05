N = int(input())
H = list(map(int, input().split()))
max = 0
cnt = 0

for i in range(N-1):
    if H[i] >= H[i+1]:
        cnt += 1
        if cnt >= max:
        max = cnt
    else:
        cnt = 0

print(max)
