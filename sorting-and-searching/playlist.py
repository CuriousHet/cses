import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

s = set()
l = 0
mx = 0

for r in range(n):
    while arr[r] in s:
        s.remove(arr[l])
        l += 1

    s.add(arr[r])
    mx = max(r-l+1, mx)

print(mx)   
