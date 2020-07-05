n = int(input())
s = list(input())

cnt = s.count("R")*s.count("G")*s.count("B")
for i in range(0, n):
    for j in range(i+1, n):
        k = 2*j - i
        if s[i] == s[j] or k >= n or s[k] == s[i] or s[k] == s[j]:
            continue
        else:
            cnt -= 1

print(cnt)
