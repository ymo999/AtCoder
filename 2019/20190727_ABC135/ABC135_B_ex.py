N = int(input())
P = list(map(int, input().split()))

cnt = 0
prev = 0

# 数列の各要素を「1,2,3,4,…,N」と比較し、異なっている箇所をカウントする
for i in range(N):
    if P[i] != i + 1:
        cnt += 1

# カウント結果が2箇所以内ならOK（1回のswapで昇順にできる）
if cnt <= 2:
    print('YES')
else:
    print('NO')
