def StalinSort(L):
    """スターリンソート
    参考
    https://qiita.com/Sirloin/items/c9e5c74be3366df65bce
    ソート対象のリストを先頭要素から調べて、昇順になっていない要素をリストで返す
    input   L:ソート対象のリスト
    output  purge:昇順になっていない（邪魔になる）要素のリスト
    """

    targ = 1
    purge = []
    for l in L:
        if l != targ:
            purge.append(l)
        else:
            targ += 1
    return purge

N = int(input())
A = list(map(int, input().split()))

if len(A) == len(StalinSort(A)):
    print(-1)
else:
    print(len(StalinSort(A)))
