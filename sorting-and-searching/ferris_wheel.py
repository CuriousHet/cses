import sys
input = sys.stdin.readline

n, w = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
i, j,cnt = 0, n-1,0

while i<=j:

    if arr[i]+arr[j] <= w:
        i+=1

    j-=1
    cnt+=1
    

print(cnt)