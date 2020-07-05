A = [list(map(int, input().split())) for i in range(3)]
N = int(input())

for _ in range(N):
  b = int(input())
  for i in range(3):
    for j in range(3):
      if A[i][j] == b:
        A[i][j] = 0

for i in range(3):
  if A[i][0] + A[i][1] + A[i][2] == 0:
    print('Yes')
    exit()

for j in range(3):
  if A[0][j] + A[1][j] + A[2][j] == 0:
    print('Yes')
    exit()

if A[0][0] + A[1][1] + A[2][2] == 0 or A[0][2] + A[1][1] + A[2][0] == 0:
  print('Yes')
  exit()

print('No')
