import math

X, Y = map(int, input().split())
mod = 1000000007

if X < 3 or Y < 3:
  print(0)
  exit()

# t=X方向に+1する回数(=Y方向に+2する回数)を仮にXと同じ値にする
t = X

# tを調整
while(t * 2 > Y):
  t -= 1
#print(t)

# r=総移動回数
r = t + (X-t)//2
#print(r)

ans = math.factorial(r) % mod
print(ans)
