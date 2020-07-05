X = int(input())

a = X // 500
b = X % 500
c = b // 5

ans = a * 1000 + c * 5
print(ans)
