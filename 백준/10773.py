arr = []
k=int(input())

for i in range(k):
    n = int(input())
    if n != 0:
        arr.append(n)
    else:
        if len(arr) != 0:
            arr.pop()

if len(arr) != 0:
    print(sum(arr))
else:
    print(0)