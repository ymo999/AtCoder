A, B = map(int, input().split())

if B == 1:
    print(0)
    exit()

tap = 0
plug = 0

while(True):
    plug = (A-1) * (tap-1) + A
    if plug >= B:
        print(tap)
        break
    tap += 1
