import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
deg = [0]*(n+1) 
starting_node = 1

for i in range(m):

    a, b = map(int, input().split())
    adj[a].append((b, i))
    adj[b].append((a, i))
    deg[a] += 1
    deg[b] += 1

# check for even degreee
for i in range(1, n+1):
    if deg[i]%2 != 0:
        print("IMPOSSIBLE")
        sys.exit()

# check connectivity
vis = [False]*(n+1)

def dfs(u):

    stack = [starting_node]
    vis[starting_node] = True

    while stack: 

        v = stack.pop()
        for y, _ in adj[v]:
            if not vis[y]:
                vis[y] = True
                stack.append(y)

dfs(1)
        
for i in range(1, n+1):
    if deg[i] > 0 and not vis[i]:
        print("IMPOSSIBLE")
        sys.exit()

# heinholzer's algo 

used_edges = [False] * m
circuit = []
stack = [starting_node]

while stack:

    v = stack[-1]

    # remove used edges
    while adj[v] and used_edges[adj[v][-1][1]]:
        adj[v].pop()
    
    # if empty add that in circuit
    if not adj[v]:
        circuit.append(v)
        stack.pop()
    
    # use that edge and add that vertex to stack 
    else:
        u, edge_id = adj[v].pop()
        if not used_edges[edge_id]:
            used_edges[edge_id] = True
            stack.append(u)

if len(circuit) != (m+1):
    print("IMPOSSIBLE")

else:
    print(*circuit[::-1])
