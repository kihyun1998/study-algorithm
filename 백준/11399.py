import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()
rst=0

for i in range(len(arr)+1):
    for j in range(i):
        rst+=arr[j]

print(rst)