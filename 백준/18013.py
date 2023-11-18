n,m = map(int,input().split())

nList = [i+1 for i in range(n)]

for case in range(m):
    i,j = map(int,input().split())
    nList[i-1],nList[j-1] = nList[j-1],nList[i-1]

for i in nList:
    print(i,end=" ")