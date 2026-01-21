# PRIM'S ALGO
import sys
# import heapq
input = sys.stdin.readline

# n, m = map(int, input().split())

# graph = [[] for _ in range(n)]

# for _ in range(m):

#     a, b, c = map(int, input().split())
#     a -= 1
#     b -= 1

#     graph[a].append((b, c))
#     graph[b].append((a, c))

# min_heap = [[0,0]]
# visted = [False]*n
# total_cost = 0

# while min_heap:

#     cost, node = heapq.heappop(min_heap)
#     if visted[node]:
#         continue

#     visted[node] = True
#     total_cost += cost

#     for enode, ecost in graph[node]:

#         if not visted[enode]:
#             heapq.heappush(min_heap, (ecost, enode))


# if all(visted):
#     print(total_cost)

# else:
#     print("IMPOSSIBLE")


# KRUSKAL ALGO

n, m = map(int, input().split())

edges = []

for _ in range(m):

    a, b, c = map(int, input().split())
    edges.append((c, a-1, b-1))

parent = list(range(n))
rank = [0] * n

def find(u):

    if parent[u] != u:
        parent[u] = find(parent[u])
    
    return parent[u]

def union(u,v):

    u = find(u)
    v = find(v)

    if u == v:
        return False

    if rank[u] > rank[v]:
        parent[v] = u
    elif rank[v] > rank[u]:
        parent[u] = v
    else:
        parent[v] = u
        rank[u] += 1
    
    return True


edges.sort()
total_cost = 0
used_edges = 0

for cost, a, b in edges:
    if union(a, b):
        total_cost += cost
        used_edges += 1 
        if used_edges == n-1:
            break

if used_edges == n-1:
    print(total_cost)
else:
    print("IMPOSSIBLE")