import sys

n,m = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().split()))

pre_sum = [0]
for i in lst:
    pre_sum.append(pre_sum[-1]+i)


for i in range(m):
    start,end = map(int, sys.stdin.readline().rstrip().split())
    print(pre_sum[end]-pre_sum[start-1])
