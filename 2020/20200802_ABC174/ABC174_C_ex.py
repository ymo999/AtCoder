K = int(input())

if K % 2 == 0:
    print(-1)
    exit()

# Kの桁数
K_str = str(K)
K_len = len(K_str)

for i in range(K_len, K):
    num_str = '7' * i
    num = int(num_str)
    if num % K == 0:
        print(i)
        exit()

print(-1)
