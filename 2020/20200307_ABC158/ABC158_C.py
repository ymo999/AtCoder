import math

A, B = map(int, input().split())

if A == 0 and B == 0:
  print(0)
  exit()

Amin = A + 0.0
Amax = A + 0.9
Bmin = B + 0.0
Bmax = B + 0.9
priceA = priceB = 0
priceAA = priceBB = 0

priceA = math.ceil(Amin / 0.08)
priceAA = math.ceil(Amax / 0.08)
priceB = math.ceil(Bmin / 0.10)
priceBB = math.ceil(Bmax / 0.10)

ansi = ansj = 0

for i in range(priceA, priceAA+1):
  if i == priceB:
    ansi = i
    break
  if i == priceBB:
    ansi = i
    break

for j in range(priceB, priceBB+1):
  if j == priceA:
    ansj = j
    break
  if j == priceAA:
    ansj = j
    break

#print(priceA, priceAA)
#print(priceB, priceBB)
#print(ansi, ansj)

if ansi == 0 and ansj == 0:
  print(-1)
else:
  if ansi ==0 or ansj == 0:
    print(max(ansi, ansj))
  else:
    print(min(ansi, ansj))
