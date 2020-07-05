def solve(n, a, b, c, d):
    num = 1             # Nの最小値は制約より1なので、初期値を1とする
    ans = d

    if n == num:        # Nが1の場合は解を出力して次のテストケースへ
        print(ans)
        return

    print(ans)
    return


T = int(input())

for t in range(T):
    N, A, B, C, D = map(int, input().split())
    solve(N, A, B, C, D)