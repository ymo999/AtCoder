'''
参考
https://qiita.com/tanakh/items/a312a9bd684658ab1e7b
左側から「白」が見つかったら、右側から見つかった「赤」と入れ替える
'''
N = int(input())
C = list(map(str, input()))

left = 0
right = N - 1
ans = 0

while True:
    while left < N and C[left] != 'W':      # 左側から「白」が見つかるまでポインタをずらしていく
        left += 1
    while right >= 0 and C[right] != 'R':   # 右側から「赤」が見つかるまでポインタをずらしていく
        right -= 1
    if left >= right:                       # 停止条件
        break
    ans += 1                                # 見つかったら解をカウントアップ（赤白入れ替え）
    left += 1
    right -= 1

print(ans)
