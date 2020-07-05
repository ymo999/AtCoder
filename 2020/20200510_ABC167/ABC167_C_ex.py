'''
参考
https://kakedashi-engineer.appspot.com/
https://note.com/sdestiny/n/nbd01567e6f7a
bit全探索を行う

※itertools.productについては以下を参照
https://note.nkmk.me/python-itertools-product/
'''
from itertools import product

N, M, X = map(int, input().split())
C = []
A = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    C.append(tmp[0])
    A.append(tmp[1:])

INF = 10**9    # 解（参考書合計価格の最小値）と比較するために便宜上設定
ans = INF

# N冊の参考書すべてについて、
# 「買う=1」「買わない=0」の組み合わせ全パターン作成し
# それぞれの組み合わせについて
# 「合計価格は最小か」「理解度はX以上になるか」を調べる
# （bit全探索）
for p in product([0, 1], repeat=N):
    skill = [0] * M     # 参考書によって上げることのできる理解度（初期化）
    cost = 0            # 参考書の価格
    for n in range(N):
        if p[n]:    # N冊目の参考書を「買う」場合
            for m in range(M):
                skill[m] += A[n][m] # その参考書で上げられる理解度を加算
            cost += C[n]
    
    if min(skill) >= X:
        ans = min(ans, cost)

if ans == INF:
    print(-1)   # ans が更新されていない（目標達成できない）
else:
    print(ans)
