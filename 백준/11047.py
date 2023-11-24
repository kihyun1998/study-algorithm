import sys
from collections import deque

arr = deque([])
count=0
n,k = map(int,sys.stdin.readline().rstrip().split())

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    arr.appendleft(x)

for i in arr:
    if k == 0:
        break
    if k >= i:
        count += (k//i)
        k %= i
    else:
        continue

print(count)