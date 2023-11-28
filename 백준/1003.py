import sys

cases = int(sys.stdin.readline().rstrip())

ans = []

for i in range(cases):
    x = int(sys.stdin.readline().rstrip())
    dp=[[0,0] for _ in range(x+1)]
    dp[0][0] = 1
    dp[0][1] = 0
    if x > 0:
        dp[1][0] = 0
        dp[1][1] = 1
        for i in range(2,x+1):
            dp[i][0] = dp[i-1][0]+dp[i-2][0]
            dp[i][1] = dp[i-1][1]+dp[i-2][1]
    
    ans.append(dp[x])

for i in ans:
    print(i[0],i[1])