import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
n = n//2

l = arr[n]
total = 0 

for a in arr:
    total += abs(a-l)

print(total)