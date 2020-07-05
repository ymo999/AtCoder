'''
参考
https://penyoo.hatenablog.com/entry/2019/12/02/045335
X を 「X//100=a…購入商品数」と「X%100=b…端数」の2つに分けて考える
※商品の価格が「100～105（100+0～100+5）」になっているため
a、bについて
    b//5!=0の場合
        b//5+1<=a
    b//5==0の場合
        b//5<=a
が成立すれば、買い物ができる

例1：X=617円の場合⇒買い物可能
a=X//100==6     b=X%100==17     b//5+1==4<=a
例2：X=489円の場合⇒買い物不可
a=X//100==4     b=X%100==89     b//5+1==18>a
'''
X = int(input())
purchase_count = X // 100
surplus = X % 100
tmp = surplus // 5

if surplus % 5 != 0:
    tmp += 1

if purchase_count >= tmp:
    print(1)
else:
    print(0)
