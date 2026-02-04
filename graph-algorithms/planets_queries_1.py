import sys
input = sys.stdin.readline

n, q = map(int, input().split())
teleports = list(map(int, input().split()))

teleports = [x-1 for x in teleports]
lg = 30

jump = [[0]*n for _ in range(lg)]

for v in range(n):
    jump[0][v] = teleports[v]

for binary in range(1, lg):
    for i in range(n):
        jump[binary][i] = jump[binary-1][jump[binary-1][i]]
    
res = []

for _ in range(q):
    x, k = map(int, input().split())
    x -= 1

    bit = 0

    while k>0:
        if k&1:
            x = jump[bit][x]
        k >>= 1
        bit += 1
    
    res.append(x+1)

for value in res:
    print(value)
