S = input()
N = len(S) - 1
ans = 0

start = 0
end = start + 3
tmp = 0

while start <= N-3:
    while end <= N-1:
        end = start + 3
        if end == N:
            tmp = int(S[start:])
        else:
            tmp = int(S[start:end])
        if tmp % 2019 == 0:
            ans += 1
        end += 1
    start += 1

print(ans)
