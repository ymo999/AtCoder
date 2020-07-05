N, M = map(int, input().split())

if N == 1 and M == 0:
  print(0)				# 1桁かつ無条件の場合は0
  exit()

sc = [list(map(int, input().split())) for i in range(M)]

ans = ['x'] * N			# 解答の整数を初期化

for i in range(M):
  s = sc[i][0]
  c = sc[i][1]
  if s == 1 and c == 0 and N != 1:
    print(-1)			# 1桁以外の整数で先頭桁が0はNG
    exit()
  if ans[s-1] == 'x':
    ans[s-1] = str(c)	# 指定桁の数値を置換
  else:
    if ans[s-1] != str(c):
      print(-1)			# 同一の桁に対して異なる数値を挿入できない
      exit()

for index, char in enumerate(ans):
  if char == 'x':
    if index == 0:
      ans[index] = '1'	# 先頭桁が未置換ならば最小値の1で置換
    else:
      ans[index] = '0'	# 先頭桁以外で未置換の桁があれば最小値の0で置換

print(int(''.join(ans)))
