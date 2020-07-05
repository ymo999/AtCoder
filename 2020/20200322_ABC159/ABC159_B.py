S = input()
N = len(S)

a = (N-1) // 2
b = (N+3) // 2

#print(S[0:a])
#print(''.join(list(reversed(S[0:a]))))
#print(S[b-1:])
#print(''.join(list(reversed(S[b-1:]))))

if S == ''.join(list(reversed(S))):
    if S[0:a] == ''.join(list(reversed(S[0:a]))):
        if S[b-1:] == ''.join(list(reversed(S[b-1:]))):
            print('Yes')
            exit()

print('No')
