from collections import deque

n = int(input())
cards = deque([x for x in range(1,n+1)])


while len(cards) != 1:
    cards.popleft()
    if len(cards) == 1:
        print(cards[0])
        break
    cards.rotate(-1)
else:
    print(cards[0])
