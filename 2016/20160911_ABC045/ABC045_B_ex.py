SA = list(map(str, input()))
SB = list(map(str, input()))
SC = list(map(str, input()))

card = SA.pop(0)

if len(SA) == 0:
    print('A')
    exit()

while True:
#    print(card)
    if card == 'a':
        if len(SA) == 0:
            print('A')
            break
        card = SA.pop(0)
    if card == 'b':
        if len(SB) == 0:
            print('B')
            break
        card = SB.pop(0)
    if card == 'c':
        if len(SC) == 0:
            print('C')
            break
        card = SC.pop(0)
