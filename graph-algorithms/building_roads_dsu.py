import sys
input = sys.stdin.readline

class DSU:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    
    def findPar(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findPar(self.parent[x])
        
        return self.parent[x]

    def union(self, x, y):

        x,y = self.findPar(x), self.findPar(y)
        if x == y:
            return
        
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[y] > self.rank[x]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += 1
                
n, m = map(int, input().split())

dsu = DSU(n+1)

for _ in range(m):

    u, v = map(int, input().split())
    dsu.union(u, v)

paths = []
for i  in range(1,n+1):
    if dsu.findPar(i) == i:
        paths.append(i)

print(len(paths)-1)
for i in range(len(paths)-1):
    print(paths[i], paths[i+1])