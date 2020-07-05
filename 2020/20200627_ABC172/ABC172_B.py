S = input()
T = input()

ans = 0

for i, s in enumerate(S):
    if s != T[i]:
        ans += 1

print(ans)
