import sys
input = sys.stdin.readline

n = input().strip()
m = input().strip()

dp = [[0]*(len(m)+1) for _ in range(len(n)+1)]

for i in range(len(n)+1): 
    dp[i][0] = i

for j in range(len(m)+1):
    dp[0][j] = j

for i in range(1,len(n)+1):
    for j in range(1,len(m)+1):

        if n[i-1] == m[j-1]:
            dp[i][j] = dp[i-1][j-1]

        else:
            dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))

print(dp[len(n)][len(m)])
