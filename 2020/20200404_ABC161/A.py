A, B, C = map(int, input().split())

# swap A<->B
tmp = A
A = B
B = tmp

# swap A<->C
tmp = A
A = C
C = tmp

print(A, B, C)
