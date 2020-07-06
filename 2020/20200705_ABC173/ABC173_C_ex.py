'''
参考
https://note.com/tanon_cp/n/n9b0a77fcda7d
https://qiita.com/u2dayo/items/90a0693f31524e7b4cd0#c%E5%95%8F%E9%A1%8Ch-and-v
bit全探索を使用する
'''
from itertools import product

H, W, K = map(int, input().split())
c = [list(input()) for _ in range(H)]

ans = 0

# bit全探索
for b_row in product([0, 1], repeat=H):             # 行の塗りつぶし全パターンを0か1で列挙
    for b_col in product([0, 1], repeat=W):         # 列の塗りつぶし全パターンを0か1で列挙
        cnt = 0
        for i in range(H):
            for j in range(W):                      # 全ての「i行目j列目」について調べる
                if b_row[i] == 0 and b_col[j] == 0: # 塗りつぶされないマス
                    if c[i][j] == '#':              # 黒のままだったらカウントアップ
                        cnt += 1
        if cnt == K:                                # 全ての「i行目j列目」についてカウント終了、黒マス数がKと一致したら
            ans += 1                                # 解答をカウントアップ

print(ans)
