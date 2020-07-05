X = int(input())
amt = 100
ans = 0

while amt < X:
    amt = int(amt * 1.01)
    ans += 1

print(ans)
