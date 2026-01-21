import sys
input = sys.stdin.readline

n = int(input())
grid = [list(input().strip()) for _ in range(n)]

dp = [[0]*n for _ in range(n)]


for i in range(n):
    if grid[i][0]=='*':
        break
    dp[i][0] = 1

for j in range(n):
    if grid[0][j]=='*':
        break
    dp[0][j] = 1

for i in range(1, n):
    for j in range(1, n):
        if grid[i][j] == '*':
            dp[i][j] = 0
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % (10**9 + 7)

print(dp[n-1][n-1]%(10**9 + 7))