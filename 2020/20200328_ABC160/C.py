K, N = map(int, input().split())
A = list(map(int, input().split()))

prev = A[0]
dist = K - A[N-1] + A[0]
for i in range(1,N):
#  print('dist=', dist)
#  print('A[i]=', A[i])
#  print('prev=', prev)
#  print('A[i]-prev=', A[i] - prev)
  if A[i] - prev > dist:
    dist = A[i] - prev
  prev = A[i]

ans = K - dist
print(ans)
