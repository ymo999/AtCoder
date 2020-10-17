N, M = map(int, input().split())
route = []

# BFS(参考：ABC168_D)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
