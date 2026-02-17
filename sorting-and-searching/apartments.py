import sys
from bisect import bisect_right
input = sys.stdin.readline

n, m, k = map(int, input().split())
applications = list(map(int, input().split()))
apartments = list(map(int, input().split()))

applications.sort()
apartments.sort()

i, j, res =  0, 0, 0

while i<n and j<m:

    if applications[i] - k > apartments[j]:
        j+=1
    elif applications[i] + k < apartments[j]:
        i+=1
    else:
        res+=1
        i+=1
        j+=1

print(res)