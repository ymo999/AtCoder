import math

N, M = map(int, input().split())

if N < 2:
    even =0
else:
    even = math.factorial(N) // (math.factorial(N - 2) * math.factorial(2))

if M < 2:
    odd = 0
else:
    odd = math.factorial(M) // (math.factorial(M - 2) * math.factorial(2))

#print(even, odd)
print(even + odd)
