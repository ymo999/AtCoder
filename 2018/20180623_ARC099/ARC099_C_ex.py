N, K = map(int, input().split())
A = list(map(int, input().split()))     # このリストは使用しない

ans = 0
done = 1

while done < N:
    done += K - 1
    ans += 1

print(ans)
