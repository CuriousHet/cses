import sys 
input = sys.stdin.readline

n, m = map(int, input().split())

a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):

        if a1[i-1] == a2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        
        else:
            dp[i][j] = max(dp[i-1][j-1],max(dp[i-1][j], dp[i][j-1]))

l = dp[n][m]
new_a = [0] * l

x = n 
y = m 

while x > 0 and y > 0:

    if a1[x-1] == a2[y-1]:
        new_a[l-1] = a1[x-1]
        l = l - 1
        x = x - 1
        y = y - 1 

    elif dp[x-1][y] > dp[x][y-1]:
        x = x - 1
    else:
        y = y - 1 

print(dp[n][m])
print(*new_a)