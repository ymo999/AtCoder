import math

X, Y = map(int, input().split())
mod = 1000000007

if X < 3 or Y < 3:
  print(0)
  exit()

# t=X������+1�����(=Y������+2�����)������X�Ɠ����l�ɂ���
t = X

# t�𒲐�
while(t * 2 > Y):
  t -= 1
#print(t)

# r=���ړ���
r = t + (X-t)//2
#print(r)

ans = math.factorial(r) % mod
print(ans)
