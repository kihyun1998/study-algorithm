## 오답임

import sys

_ = int(sys.stdin.readline())
cards = map(int,sys.stdin.readline().split())
_ = int(sys.stdin.readline())
input_keys = map(int, sys.stdin.readline().split())

keys = list(input_keys).copy()

dic = {key:0 for key in keys}

for card in cards:
    if card in dic:
        dic[card] += 1


for key in keys:
    print(dic.get(key),end=" ")