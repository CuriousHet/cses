import sys
from bisect import bisect_right
input = sys.stdin.readline

n, m = map(int, input().split())
tickets = sorted(map(int, input().split()))
cust = list(map(int, input().split()))
parent = list(range(n))

res = []

def find(x):

    if x < 0:
        return -1
    
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

for val in cust:

    idx = bisect_right(tickets, val) - 1
    idx = find(idx)

    if idx == -1:
        res.append(-1)
    
    else:
        res.append(tickets[idx])
        parent[idx] = find(idx-1)

for val in res:
    print(val)