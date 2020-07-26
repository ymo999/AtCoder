A, B, C = map(int, input().split())
K = int(input())

for _ in range(K):
    if C <= B or C <= A:
        C = C * 2
        continue
    if B <= A:
        B = B * 2
    else:
        C = C * 2

if A < B and B < C:
    print('Yes')
else:
    print('No')
