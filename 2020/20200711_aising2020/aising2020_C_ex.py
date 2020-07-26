N = int(input())
ans = [0] * N

for x in range(1, int(N**0.5)+1):
    for y in range(1, int(N**0.5)+1):
        for z in range(1, int(N**0.5)+1):
            n = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if n <= N:
                ans[n-1] += 1

for n in range(N):
    print(ans[n])
