A, B, C, D = map(int, input().split())

if A <= C and C <= B:
    print('Yes')
elif C <= A and A <= D:
    print('Yes')
else:
    print('No')
