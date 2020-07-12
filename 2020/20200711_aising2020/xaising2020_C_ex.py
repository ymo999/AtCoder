N = int(input())

for n in range(1, N+1):
    ans = 0
    for x in range(1, N+1):
        for y in range(1, N-x+1):
            for z in range(1, N-x-y+1):
                if x**2 + y**2 + z**2 + x*y + y*z + z*x == n:
                    ans += 1
    print(ans)
