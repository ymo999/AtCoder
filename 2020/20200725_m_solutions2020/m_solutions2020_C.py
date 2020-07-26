N, K = map(int, input().split())
A = list(map(int, input().split()))

p_score = 0
score = 0
tmp = []

for n in range(K-1, N):
    if n > K-1:
        score -= A[n-K]
        score += A[n]
        if score > p_score:
            print('Yes')
        else:
            print('No')
    else:
        tmp = A[n-(K-1):n+1]
        # print(tmp)
        score = sum(tmp)
    p_score = score
