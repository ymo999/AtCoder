n,x,y = map(int, input().split())
x -= 1
y -= 1

ans = [0] * (n-1)

for j in range(n):
  for i in range(j):
    ans[min(j-i, abs(x-i)+1+abs(j-y)) - 1] += 1

print("\n".join([str(d) for d in ans]))
