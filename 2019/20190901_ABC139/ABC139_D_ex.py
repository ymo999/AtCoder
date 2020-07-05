'''
参考
https://qiita.com/DaikiSuyama/items/ddb4544ee5df2f8d45c7
1～Nをある数で割った余りの合計を最大値にするためには、
2～Nで1～N-1を割ればよい（最後のNは1で割る）
以下の通り、余りは1～Nとなる
1 mod 2 = 1
2 mod 3 = 2
3 mod 4 = 3
…
（N-1) mod N = N-1
N mod 1 = N
https://mathwords.net/1karannowa
1～Nまでの和を求める公式
'''

N = int(input())
ans = N * (N-1) // 2
print(ans)
