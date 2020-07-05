n, x = map(int, input().split())
l = list(map(int, input().split()))

pre_coordinate = 0
ans = 1

for i in range(1, n+1):
    coordinate = pre_coordinate + l[i-1]
    if coordinate > x:
        break
    pre_coordinate = coordinate
    ans += 1

print(ans)
