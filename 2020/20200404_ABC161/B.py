N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

lim = sum(A) / 4 / M
ans = A[:M]

for a in ans:
  if a < lim:
    print('No')
    exit()

print('Yes')
