from operator import itemgetter

N = int(input())
book = []

for i in range(N):
    S, P = map(str, input().split())
    book.append([S, int(P), i+1])

book = sorted(book, key=itemgetter(1), reverse=True)
book = sorted(book, key=itemgetter(0))
#print(book)

for ans in book:
    print(ans[2])
