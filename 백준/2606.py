import sys

def bfs(s):
    q=[]
    q.append(s)
    visited[s]=True

    while q:
        now = q.pop(0)
        for next in arr[now]:
            if not visited[next]:
                q.append(next)
                visited[next]=True

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

arr = [[] for _ in range(n+1)]
for _ in range(m):
    start,end = map(int, sys.stdin.readline().rstrip().split())
    arr[start].append(end)
    arr[end].append(start)

visited=[False]*(n+1)
bfs(1)

# 시작값도 포함이 되어 추후에 1을 빼기 싫어서 빼진상태로 시작
cnt = -1

for v in visited:
    if v:
        cnt+=1

print(cnt)