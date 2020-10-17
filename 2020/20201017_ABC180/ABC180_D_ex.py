'''
解説
https://atcoder.jp/contests/abc180/editorial/219
'''
X, Y, A, B = map(int, input().split())
str = X
exp = 0
tmp1 = 0    # カコモンジム
tmp2 = 0    # AtCoderジム

while(True):
    tmp1 = str * A
    tmp2 = str + B
    if min(tmp1, tmp2) >= Y:
        break
    str = min(tmp1, tmp2)
    exp += 1

print(exp)
