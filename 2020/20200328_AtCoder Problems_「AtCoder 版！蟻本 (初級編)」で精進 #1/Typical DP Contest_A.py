'''
A - �R���e�X�g_Typical DP Contest
https://atcoder.jp/contests/tdpc/tasks/tdpc_contest
���Q�l
https://qiita.com/aki-takano/items/54b6571c6771407063dc
'''

# input
N = int(input())
p = list(map(int, input().split()))

# i��ڂ܂ł̖����g����j�_�̍��v�_���ł��邩
DP = []

for i in range(1, N+1):
  

'''
loop(1���-N���)
DP[i-1]�̏�Ԃ�����DP[i]�ɒl����
'''
for i in range(1, N+1):
  for j, j_status in enumerate(DP[i-1]):


