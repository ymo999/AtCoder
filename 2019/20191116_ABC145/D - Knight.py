import math

X, Y = map(int, input().split())
mod = 1000000007

if X < 3 or Y < 3:
  print(0)
  exit()

# t=X•ûŒü‚É+1‚·‚é‰ñ”(=Y•ûŒü‚É+2‚·‚é‰ñ”)‚ğ‰¼‚ÉX‚Æ“¯‚¶’l‚É‚·‚é
t = X

# t‚ğ’²®
while(t * 2 > Y):
  t -= 1
#print(t)

# r=‘ˆÚ“®‰ñ”
r = t + (X-t)//2
#print(r)

ans = math.factorial(r) % mod
print(ans)
