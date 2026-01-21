import sys
input = sys.stdin.readline

n, target = map(int, input().split())
coins = list(map(int, input().split()))

MOD = 10**9 + 7

dp = [0]*(target+1)
dp[0] = 1 
# coins.sort()

for i in range(1, target + 1):
    total = 0
    for c in coins:
        if i >= c:
            total += dp[i - c]
    dp[i] = total % MOD

print(dp[target])
