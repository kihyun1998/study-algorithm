import sys

def calc(start,end,lans,n):
    if end-start <= 1:
        return start
    mid = (start + end) // 2
    count = 0
    for lan in lans:
        count += (lan//mid)
    if count < n:
        return calc(start,mid,lans,n)
    else:
        return calc(mid,end,lans,n)

lans = []
big=0
k, n = map(int, sys.stdin.readline().rstrip().split())

for _ in range(k):
    x = int(sys.stdin.readline().rstrip())
    big = max(big,x)
    lans.append(x)

print(calc(1,big+1,lans,n))