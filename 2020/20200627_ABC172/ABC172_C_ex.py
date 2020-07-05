N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 累積和の算出
A_sum, B_sum = [0], [0]
for i, a in enumerate(A):
    A_sum.append(A_sum[i] + a)
for i, b in enumerate(B):
    B_sum.append(B_sum[i] + b)

ans = 0
j = M

# 机Aの本を読む所要時間:A_sum[i] … iの値を0から増やしていく
# 机Bの本を読む所要時間:B_sum[j] … iの値を固定し、Mから減らしていく
# A_sum[i]+B_sum[j]がKに収まるiとjの値を見つけ出し、i+jの値を出す
# iの値を増やしながら上記を繰り返し、i+jの最大値が解となる
for i in range(N+1):
    if A_sum[i] > K:
        break
    while B_sum[j] > K - A_sum[i]:
        j -= 1
    ans = max(ans, i+j)

print(ans)
