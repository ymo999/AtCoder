'''
参考
https://qiita.com/u2dayo/items/acfeb20a912b04276641#c%E5%95%8F%E9%A1%8Ca-x-b--c

A*B+C=n ⇒ C=n-A*B
'''
# 提出PyPy3

def solve(n):
    ans = 0
    for a in range(1, n):
        for b in range(1, n):
            c = n - a * b
            if c <= 0:
                break
            ans += 1
    return ans

N = int(input())
ans = solve(N)
print(ans)
