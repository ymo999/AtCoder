'''
参考
https://note.com/tanon_cp/n/n6b51b9a57076
'''
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
spl = 0                     # 1つ前の勇者の余力
B.append(0)                 # リストの要素数を調整

for i in range(N+1):
    ans += min(spl, A[i])   # まず1つ前の勇者の余力を討伐に充てる
    mst = max(0, A[i]-spl)  # モンスター残数

    ans += min(B[i], mst)
    spl = max(0, B[i]-mst)

print(ans)
