## 오답임

import sys

_ = int(sys.stdin.readline())
cards = map(int,sys.stdin.readline().split())
_ = int(sys.stdin.readline())
keys = map(int, sys.stdin.readline().split())

dic = {key:0 for key in keys}

for card in cards:
    if card in dic:
        dic[card] += 1

for v in dic.values():
    print(v,end=" ")