'''
参考
https://kakedashi-engineer.appspot.com/2020/03/23/abc159d/
https://qiita.com/c-yan/items/83ae14b2fbf117355586
kを抜かない場合の方法の数を出し、そこからkを選ぶ場合の数を引く
'''
import collections

N = int(input())
A = list(map(int, input().split()))

# ボールに書かれた整数と、その個数の辞書を作成
D = collections.Counter(A)
L = {}
total = 0

# 辞書の整数=k、個数=vごとに
# その整数の個数の辞書=Lと
# 組み合わせ総数=totalを出す
for k, v in D.most_common():
    L[k] = v
    total += v * (v-1) // 2

for a in A:
    print(total - (L[a]-1))
