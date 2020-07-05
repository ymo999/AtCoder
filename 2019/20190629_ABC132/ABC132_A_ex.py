s = input()
tmp = set(s)

if len(tmp) == 2:
    for c in tmp:
        if s.count(c) != 2:
            print('No')
            exit()
    print('Yes')
else:
    print('No')