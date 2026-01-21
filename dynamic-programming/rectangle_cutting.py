import sys
input = sys.stdin.readline

n, m = map(int, input().split())
if n > m: 
    n, m = m, n 

dp = [[10**9]*(m+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    for j in range(i, m+1):

        if i == j: 
            dp[i][j] = 0
        else:
            for k in range(1, i//2 + 1):
                dp[i][j] = min(dp[i][j], 1 + dp[k][j] + dp[i-k][j])

            # vertical cuts (normalize indices)
            for k in range(1, j//2 + 1):
                a, b = min(i, k), max(i, k)
                c, d = min(i, j-k), max(i, j-k)
                dp[i][j] = min(dp[i][j], 1 + dp[a][b] + dp[c][d])
    
print(dp[n][m])