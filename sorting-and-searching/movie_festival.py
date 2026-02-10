import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):

    a, b = map(int, input().split())
    arr.append((a,b))

last, cnt = -1, 1
arr.sort(key=lambda x: x[1])

for x, y in arr:

    if last == -1:
        last = y
    
    elif x >= last:
    
        # print(f"taken: {x}, {y}, {last}")
        last = y
        cnt += 1

print(cnt)