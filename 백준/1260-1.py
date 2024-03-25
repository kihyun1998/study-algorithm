import sys
from collections import deque

"""
이번 노드에서 할일을 정의하고 다음 노드를 어디로 갈지
1. 현재 노드 방문 표시
2. 정답에 추가
"""
def dfs(v):
    rst_dfs.append(v)
    visited[v]=True

    for next in arr[v]:
        if not visited[next]:
            dfs(next)

"""
1. 덱구성
2. 초기 노드 덱에 추가
3. 덱에 초기 노드와 연결된 노드들 추가
4. 선입 선출하면서 순회
"""
def bfs(v):
    q = deque()
    q.append(v)
    rst_bfs.append(v)
    visited[v] = True
    while(q):
        current = q.popleft()
        for next in arr[current]:
            if not visited[next]:
                q.append(next)
                rst_bfs.append(next)
                visited[next]=True



"""
n = 정점
m = 간선
v = 시작 정점 번호
"""
n,m,v = map(int,sys.stdin.readline().rstrip().split())


arr = [[] for _ in  range(n+1)]

for _ in  range(m):
    s,e = map(int,sys.stdin.readline().rstrip().split())
    arr[s].append(e)
    arr[e].append(s)

for i in range(1,n+1):
    arr[i].sort()

visited = [False for _ in range(n+1)]
rst_dfs = []
dfs(v)

for rst in rst_dfs:
    print(rst,end=" ")

print()
visited = [False for _ in range(n+1)]
rst_bfs = []
bfs(v)
for rst in rst_bfs:
    print(rst,end=" ")