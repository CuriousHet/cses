import sys
from bisect import bisect_right
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

tow = []

for val in arr:
    id = bisect_right(tow, val)
    if id == len(tow):
        tow.append(val)
    else:
        tow[id] = val

print(len(tow))