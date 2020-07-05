N, K = map(int, input().split())
diff = abs(N - K)

while(N > diff):
  max_num = max(N, K)
  min_num = min(N, K)
  N = max_num % min_num
  diff = abs(N - K)

print(N)
