n = int(input())
a = [int(input()) for _ in range(n)]
#print(a)
a_sort = sorted(a)
#print(a_sort)

max_number = a_sort[-1]
sub_max_number = a_sort[-2]

for i in range(n):
  if a[i] == max_number:
    print(sub_max_number)
  else:
    print(max_number)
