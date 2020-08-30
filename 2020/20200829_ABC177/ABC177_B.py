# 提出はPyPy3

def count_diff(a, b):
    cnt = 0
    for c_a, c_b in zip(a, b):
        if c_a != c_b:
            cnt += 1
    return cnt

S = input()
T = input()

if len(S) == len(T):
    ans = count_diff(S, T)
    print(ans)
    exit()

ans = float('inf')
for i in range(len(S)-len(T)):
    word = S[i:i+len(T)]
    tmp = count_diff(word, T)
    ans = min(ans, tmp)

print(ans)
