N, A, B = map(int, input().split())

if N == 0:
  print(0)
  exit()

cnt = N // (A + B)
rem = N % (A + B)

ans = 0

if rem >= A:
  ans = A * (cnt + 1)
else:
  ans = A * cnt + rem

print(ans)
