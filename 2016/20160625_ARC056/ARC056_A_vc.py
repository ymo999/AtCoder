A, B, K, L = map(int, input().split())


if B < A * L:
    bara = K % L
    oset = K // L
    ans = min(oset*B+bara*A, (oset+1)*B)
else:
    ans = A * K

print(ans)
