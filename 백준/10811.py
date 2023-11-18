n,m = map(int, input().split())

nList = [i+1 for i in range(n)]

for i in range(m):
    i,j = map(int, input().split())
    nList[i-1:j] = reversed(nList[i-1:j])

for i in nList:
    print(i,end=" ")