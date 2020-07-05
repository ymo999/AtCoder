X, Y = map(int, input().split())
C = 2
T = 4

for t in range(X+1):
    if t * T + (X-t) * C == Y:
        print('Yes')
        exit()

print('No')
