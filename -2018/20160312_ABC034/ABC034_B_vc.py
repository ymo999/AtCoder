N, D = map(int, input().split())
drange = D * 2 + 1

if N % drange == 0:
    print(N//drange)
else:
    print(N // drange + 1)
