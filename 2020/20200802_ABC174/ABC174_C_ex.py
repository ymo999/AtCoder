'''
参考
https://qiita.com/c-yan/items/d1b19114d411755f25b5
https://qiita.com/easychoco/items/7f1f00d9221bd3ab0a6c
数列は以下で表すことができる
a[n+1] = a[n] * 10 + 7
a[n] % K == 0となれば、その時点でのnが解となる
'''
K = int(input())
if K % 2 == 0:
    print(-1)
    exit()

num = 0

for i in range(K):
    num = (num * 10 + 7) % K
    if num == 0:
        print(i+1)
        exit()

print(-1)
