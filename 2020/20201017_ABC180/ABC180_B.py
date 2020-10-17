N = int(input())
X = list(map(int, input().split()))

man = 0
euc = 0
che = -10 ** 6

for x in X:
    man += abs(x)
    euc += abs(x)**2
    che = max(che, abs(x))

print(man)
print(euc**0.5)
print(che)
