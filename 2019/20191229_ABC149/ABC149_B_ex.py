A, B, K = map(int, input().split())

if K == 0:
    print(A, B)
    exit()

if A - K >= 0:
    print(A-K ,B)
elif A + B - K >= 0:
    print(0, A+B-K)
else:
    print(0, 0)
