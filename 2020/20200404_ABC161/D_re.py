K=int(input())+1

def dfs(n,f,l,s):
  global K
  if l==0:
    K-=1
    if K==0:
      print(n)
      exit()
  elif s==1:
    for i in range(0,10):
      if i==0:
        dfs(10*n+i,i,l-1,1)
      else:
        dfs(10*n+i,i,l-1,0)
  else:
    if f==0:
      for i in range(0,2):
        dfs(10*n+i,i,l-1,0)
    elif f==9:
      for i in range(8,10):
        dfs(10*n+i,i,l-1,0)
    else:
      for i in range(f-1,f+2):
        dfs(10*n+i,i,l-1,0)
      
dfs(0,0,10,1)
