S = input()

ans = 0
cnt = 0

for d in S:
    if d == 'R':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)

print(ans)
