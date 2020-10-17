'''
参考
https://qiita.com/u2dayo/items/f685997847d583227d06#c%E5%95%8F%E9%A1%8Cneq-min
'''
N = int(input())
P = list(map(int, input().split()))

ans = 0
is_used = [False] * 200010      # 要素を多めにとる（一応）

for n in range(N):
    is_used[P[n]] = True
    while is_used[ans]:
        ans += 1
    print(ans)
