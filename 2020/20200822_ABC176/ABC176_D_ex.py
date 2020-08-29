'''
参考
https://qiita.com/K_SIO/items/6dc5241c7ff9658841d4
'''
from collections import deque

H, W = map(int, input().split())
C = list(map(int, input().split()))
D = list(map(int, input().split()))
S = [list(input()) for _ in range(H)]

# 便宜上、CとDの各要素を-1する（indexとそろえる）
C = list(map(lambda c: c-1, C))
D = list(map(lambda d: d-1, D))

visited = [[-1] * W for _ in range(H)]
visited[C[0]][C[1]] = 0                         # スタート地点
move_A = [(1, 0), (0, 1), (-1, 0), (0, -1)]     # 移動A

main_q = deque()
magic_q = deque()

# 幅優先探索（立ち寄った箇所を0で上書き）

