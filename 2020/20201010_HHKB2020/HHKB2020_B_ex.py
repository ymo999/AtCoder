H, W = map(int, input().split())
S = []

for _ in range(H):
    S.append(input())

ans = 0

for h in range(H):
    for w in range(1, W):
        if S[h][w-1] == '.' and S[h][w] == '.':
            ans += 1

for w in range(W):
    for h in range(1, H):
        if S[h-1][w] == '.' and S[h][w] == '.':
            ans += 1

print(ans)
