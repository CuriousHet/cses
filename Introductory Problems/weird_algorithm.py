import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(1)
else:
    res = [n]
    while n != 1:
        if n%2==0:
            n = n//2    
        else:
            n = n*3 + 1

        res.append(n)
    
    print(*res)