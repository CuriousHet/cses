import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):

    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1]*(n+1)
parent = [-1]*(n+1)

q = deque()
q.append(1)
dist[1] = 0 

while q:

    u = q.popleft()
    for v in graph[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            parent[v] = u
            q.append(v)

if dist[n] == -1:
        print("IMPOSSIBLE")
        sys.exit()

path = []
curr = n

while curr != -1:
    path.append(curr)
    curr = parent[curr]

path.reverse()
print(len(path))
print(*path)