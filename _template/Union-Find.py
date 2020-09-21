'''
https://at274.hatenablog.com/entry/2018/02/02/173000
https://note.nkmk.me/python-union-find/
https://qiita.com/Kerzival/items/6923c2eb3b91be86f19f
'''

class UnionFind:
        '''
        n個の要素を1～nの番号で管理する。以下の属性およびメソッドを持つ
        parents:
            各要素の親要素の番号を格納するリスト
            要素が根（ルート）の場合は-(そのグループの要素数)を格納する
        rank:
            木の高さを格納（初期状態は0）
        find(x):
            要素xが属するグループの根を返す
        union(x, y):
            要素xが属するグループと要素yが属するグループとを併合する
        size(x):
            要素xが属するグループのサイズ（要素数）を返す
        issame(x, y):
            要素x, yが同じグループに属するかどうかを返す
        '''
    
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * (n)
        
    def find(self, x):
        if self.parents[x] < 0:     # 根ならその番号を返す
            return x
        else:                       # 根でないならその要素で再検索
            self.parents[x] = self.find(self.parents[x])    # 走査過程で親を書き換え
            return self.parents[x]
        
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:                  # 既に同じ木に属している場合
            return
        
        # 違う木に属している場合は高い方の木に低い方を併合
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]  # 併合される側の要素数を加算
        self.parents[y] = x                 # 併合する側の親を書き換え
    
    def size(self, x):
        return -self.parents[self.find(x)]
    
    def issame(self, x, y):
        return self.find[x] == self.find(y)

