import sys

def dfs(start):
    rst_dfs.append(start)
    visited[start]=True

    for num in arr[start]:
        if not visited[num]:
            dfs(num)

def bfs(start):
    q=[]
    q.append(start)
    rst_bfs.append(start)
    visited[start]=True

    while q:
        now = q.pop(0)
        for next in arr[now]:
            if not visited[next]:
                q.append(next)
                rst_bfs.append(next)
                visited[next]=True
        


n,m,v = map(int, sys.stdin.readline().rstrip().split())

arr = [ [] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    # 양방향이라 두번 append
    arr[start].append(end)
    arr[end].append(start)

for i in range(1,n+1):
    arr[i].sort()


visited = [False]*(n+1)
rst_dfs=[]
dfs(v)

print(*rst_dfs)


visited = [False]*(n+1)
rst_bfs=[]
bfs(v)

print(*rst_bfs)