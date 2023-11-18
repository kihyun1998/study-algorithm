import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())

arr = deque([x for x in range(1,n+1)])
result = []

while arr:
    arr.rotate(-(k-1))
    result.append(str(arr.popleft())) 

print("<",", ".join(result),">",sep="")