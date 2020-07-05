'''
参考
https://drken1215.hatenablog.com/entry/2019/06/29/224100
dをソートし、d[N//2]-d[N//2-1]が解
'''
n = int(input())
d = list(map(int, input().split()))
d.sort()

print(d[n//2]-d[n//2-1])
