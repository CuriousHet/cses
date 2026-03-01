import sys
input = sys.stdin.readline

n = int(input())
while n:

    a, b = map(int, input().split())
    if (a+b)%3==0 and min(a,b)*2 >= max(a,b):
        print("YES")
    else:
        print("NO")

    n-=1