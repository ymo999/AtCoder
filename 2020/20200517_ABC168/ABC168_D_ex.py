'''
参考
https://www.charter-blog.com/entry/2020/05/18/163000#D--Double-Dots
https://atcoder.jp/contests/abc168/submissions/13442966
BFS（幅優先探索について）
https://qiita.com/drken/items/996d80bcae64649a6580
'''
import collections

N, M = map(int, input().split())
'''
グラフ入力を受け取るためのリストを準備（部屋数分のリスト要素）
（2次元配列の初期化方法に注意）
https://note.nkmk.me/python-list-initialize/
'''
graph = [[] for _ in range(N+1)]    # グラフを用意（本来なら必要なのは部屋数分だがindex+1して出力するのが煩雑なので+1しておく）

for _ in range(M):                  # グラフ入力を受け取る（各通路がどの部屋間をつないでいるか）
    A, B = map(int, input().split())
    graph[A].append(B)              # Aで指定した部屋から通じる部屋Bの番号をAからの通路リストに追加
    graph[B].append(A)              # Bも同様

q = collections.deque([1])          # グラフから取り出した、通路がつながった先の部屋番号を格納するキュー
dest = [-1] * (N+1)                 # 全部屋を「未訪問」で初期化
dest[0] = 1                         # リストの先頭（出力対象外）は「1」にしておく
dest[1] = 1                         # 部屋1も訪問済ということにする（目的地なので）

while q:
    room = q.popleft()              # キューの先頭要素である部屋番号を取り出す（ここをリストにしてしまっていると計算量が増大する）
    for n_room in graph[room]:      # 部屋からの全ての通路で行ける次の部屋について
        if dest[n_room] == -1:
            dest[n_room] = room     # 今いる部屋の番号を格納
            q.append(n_room)        # キューの末尾に次の部屋を追加

if -1 in dest:
    print('No')
else:
    print('Yes')
    print('\n'.join(map(str, dest[2:])))    # 出力は2番目の部屋以降
