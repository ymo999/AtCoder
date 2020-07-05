'''
参考
https://www.planeta.tokyo/abc-129
'''
N = int(input())
W = list(map(int, input().split()))

weight_forward = 0
weight_backward = sum(W)
ans = sum(W)

for i in range(N):
    weight_forward += W[i]
    weight_backward -= W[i]

    ans = min(ans, abs(weight_backward - weight_forward))

print(ans)
