'''
参考
https://qiita.com/srtk86/items/874639e361917e5016d4

整数Nが素数である=√N以下のすべての数で割り切れない
'''
import math

def is_prime(n):
    if n == 1:
        return False
    
    for m in range(2, int(math.sqrt(n)+1)):
        if n % m == 0:
            return False
    
    return True

X = int(input())

while True:
    if is_prime(X) == True:
        break
    X += 1

print(X)
