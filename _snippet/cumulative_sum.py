from itertools import accumulate

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 累積和
A_sum = list(accumulate(A, initial=0))
B_sum = list(accumulate(B, initial=0))
