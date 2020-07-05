X = int(input())

'''
N**5 - (N-1)**5 <= 1000000000 となるNの絶対値を求めておく

N = 0
while True:
    if N**5 - (N-1)**5 > 1000000000:
        print(N)
        break
    N += 1

N = 120 となるため、-120から120を全探索の範囲にする
'''

for A in range(-120, 120):
    for B in range(-120, 120):
        if A**5 - B**5 == X:
            print(A, B)
            exit()
