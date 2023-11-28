import sys


n = int(sys.stdin.readline().rstrip())

dp = [0 for _ in range(n+1)]

for i in range(2,n+1):
    ans=[]
    ans.append(dp[i-1]+1)
    if i%2==0:
        ans.append(dp[i//2]+1)
    if i%3==0:
        ans.append(dp[i//3]+1)    
    dp[i]=min(ans)
    print("i is",i)
    print("ans is",ans)
    print("dp[i] is ",dp[i])
    print("===========")

print(dp[n])