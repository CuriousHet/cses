import sys
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):

    val = list(map(int, input().split()))
    q.append(val)

for val in q:

    x, a, b = val
    
    arr1 = list(range(1,x+1))
    arr2 = list(range(1,x+1))
    if a == 0 and b == 0:
        print("YES")
        print(*arr1)
        print(*arr2)
    
    elif a == 0 or b == 0 or a + b > x:
        print("NO")

    else:
        print("YES")
        i = x-a-b
        arr2[i+b:x] = arr1[i:i+a]
        arr2[i:i+b] = arr1[x-b:x]
 
        print(*arr1)
        print(*arr2)

