N = input()
N_sum = 0

for num in N:
    N_sum += int(num)

if N_sum % 9 == 0:
    print('Yes')
else:
    print('No')
