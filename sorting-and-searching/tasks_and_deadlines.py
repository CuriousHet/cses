import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))

arr.sort()
dl, res = 0, 0

for a,b in arr:
    res += (b-a-dl)
    dl += a

print(res)
