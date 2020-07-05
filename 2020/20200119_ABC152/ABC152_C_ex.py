N = int(input())
P = list(map(int, input().split()))

'''
参考
https://cocoinit23.com/abc152/
すべての(i, j)を調べていると制限時間を超過してしまう。
listの2つ目の要素(index=1)から順に見ていって、最小値が更新されたら解をカウントアップする。
ただし、解の最小値は常に1となるので、解の初期値は1にしておくこと。
'''
ans = 1
min_p = P[0]

for i in range(1, N):
    if P[i] <= min_p:
        min_p = P[i]
        ans += 1

print(ans)
