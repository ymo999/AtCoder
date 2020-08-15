X, K, D = map(int, input().split())

X = abs(X)

if X >= K * D:
    print(abs(X - K * D))
    exit()

mov = X // D    # 0～Xの間で移動する回数

if abs(X-mov*D) > abs(X-(mov+1)*D):
    mov += 1

rem = abs(X-mov*D)
mov = K - mov   # 残回数（あとは地点0付近を行ったり来たりするだけ）
mov = mov % 2

print(abs(rem-mov*D))
