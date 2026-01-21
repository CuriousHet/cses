import sys 
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

mx, s = arr[0], 0

for i in range(n):
    mx = max(mx, arr[i])
    s += arr[i]

print(max(2*mx, s))
