'''
参考
https://drken1215.hatenablog.com/entry/2020/05/02/225600

int(A*x/B) - A * int(x/B) の値は、Bごとに周期的になる
よって、x = min(B-1, N)となる
'''
A, B, N = map(int, input().split())
x = min(B-1, N)

print(int(A*x/B) - A * int(x/B))
