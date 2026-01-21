import sys
input = sys.stdin.readline

n, t = map(int, input().split())
arr = list(map(int, input().split()))

def can_make(time):

    total = 0
    for a in arr:
        total += time // a
        if total >= t:
            return True
    
    return False

l, r = 0, min(arr)*t
ans = r
while l <= r:

    m = (l + r) // 2
    if can_make(m):
        ans = m
        r = m - 1
    else:
        l = m + 1

print(ans)


