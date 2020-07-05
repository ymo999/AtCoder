k = int(input())
dp = [[0]*10 for i in range(12)]  # dp[i][j]: i桁で先頭がj

for i in range(10):
    dp[1][i] = 1

for i in range(1,10):
    for j in range(10):
        dp[i+1][j] += dp[i][j]
        if j<9:
            dp[i+1][j] += dp[i][j+1]
        if j>0:
            dp[i+1][j] += dp[i][j-1]

ans = 0
for i in range(11):
    for j in range(1,10):
        if k > dp[i][j]:
            k -= dp[i][j]
        else:
            ni = i-1
            nj = j
            ans = j
            break
    if ans > 0:
        break


while ni > 0:
    for j in range(nj-1,nj+2):
        if j<0 or j>9:
            continue
        if k > dp[ni][j]:
            k -= dp[ni][j]
        else:
            ans = ans*10+j
            nj = j
            break
    ni -= 1
print(ans)
