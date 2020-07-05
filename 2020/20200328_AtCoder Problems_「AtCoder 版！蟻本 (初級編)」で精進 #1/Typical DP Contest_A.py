'''
A - コンテスト_Typical DP Contest
https://atcoder.jp/contests/tdpc/tasks/tdpc_contest
▼参考
https://qiita.com/aki-takano/items/54b6571c6771407063dc
'''

# input
N = int(input())
p = list(map(int, input().split()))

# i問目までの問題を使ってj点の合計点ができるか
DP = []

for i in range(1, N+1):
  

'''
loop(1問目-N問目)
DP[i-1]の状態を見てDP[i]に値を代入
'''
for i in range(1, N+1):
  for j, j_status in enumerate(DP[i-1]):


