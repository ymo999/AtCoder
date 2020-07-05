S = input()
T = input()
cnt = 0

for i, s in enumerate(S):
    if s == T[i]:
        cnt += 1

print(cnt)
