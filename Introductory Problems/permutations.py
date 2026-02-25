import sys
input = sys.stdin.readline

n = int(input())
res = [0]*n
if n==1:
    print(1)
elif n<=3:
    print("NO SOLUTION")
elif n==4:
    res = [2, 4, 1, 3]
    print(*res)
else:
    k = 1
    for i in range(0,n,2):
        res[i] = k
        k+=1

    for i in range(1,n,2):
        res[i] = k
        k += 1

    print(*res)