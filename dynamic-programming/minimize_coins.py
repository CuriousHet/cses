n , target = map(int, input().split())  
coins = list(map(int, input().split()))

INF = 10**9
dp = [INF]*(target+1)

dp[0] = 0 
coins.sort()

for i in range(1, target+1):

    for coin in coins:
        if coin > i:
            break
        dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[target] if dp[target] != INF else -1)