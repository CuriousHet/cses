import sys
input = sys.stdin.readline

n = int(input())
sum = n*(n+1)//2

if sum%2!=0:
    print("NO")
else:
    print("YES")
    target = sum//2
    s1, s2 = [], []

    for val in range(n,0,-1):

        if target >= val:
            target -= val
            s1.append(val)
        else:
            s2.append(val)
    
    print(len(s1))
    print(*s1)
    print(len(s2))
    print(*s2)
   
