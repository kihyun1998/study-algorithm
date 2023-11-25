import sys

"""
지금은 모든 노드를 검사한다.

이것이 아닌 모든 경우의 수를 검사하고 최소값 출력하는 걸로 변경해야 한다.
"""

def bfs(x,y):
    q=[]
    q.append([x,y])
    cnt=0
    maze[x][y]=0

    while q:
        exist=False
        now = q.pop(0)
        x = now[0]
        y = now[1] 
        # 우
        if x+1 < n and maze[x+1][y] == 1:
            q.append([x+1,y])
            maze[x+1][y]=2
            exist=True 
        # 좌
        if x-1 >= 0 and maze[x-1][y] == 1:
            q.append([x-1,y])
            maze[x-1][y]=2
            exist=True
        # 하
        if y+1 < m and maze[x][y+1] == 1:
            q.append([x,y+1])
            maze[x][y+1]=2
            exist=True
        # 상
        if y-1 >= 0 and maze[x][y-1] == 1:
            q.append([x,y-1])
            maze[x][y-1]=2
            exist=True
        print("now is",now)
        print("q is ",q)
        print("====maze is====")
        for i in maze:
            print(i)
        print("===============")
        if exist:
            cnt+=1
        print("cnt is",cnt)
        print("\n\n")
    return cnt
        


n,m = map(int, sys.stdin.readline().rstrip().split())

maze = [[] for i in range(n)]

for i in range(n):
    x = list(map(int, list(sys.stdin.readline().rstrip())))
    maze[i] = x

cnt = bfs(0,0)

print(cnt)