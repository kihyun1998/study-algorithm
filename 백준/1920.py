import sys

_ = int(sys.stdin.readline())
nums = map(int, sys.stdin.readline().split())
_ = int(sys.stdin.readline())
checks = map(int, sys.stdin.readline().split())

keys = list(nums).copy()

dic = {key:0 for key in keys}

for check in checks:
    if dic.get(check) == None:
        print(0)
    else:
        print(1)