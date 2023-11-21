from collections import deque

rst=[]
test_case = int(input())

for i in range(test_case):
    cnt=0

    n,m = map(int,input().split())
    queue = deque()

    arr = map(int, input().split())
    arr_r = list(arr).copy()

    for i in range(n):
        queue.append((i,arr_r[i]))
    
    while queue:
        maxVal = max(queue, key=lambda q:q[1] )
        # 최대값과 데크 맨앞 값이 같은 경우
        if maxVal[1] == queue[0][1]:
            cnt+=1
            # 이 값이 찾고 있는 순서의 문서인 경우
            if m == queue[0][0]:
                
                rst.append(cnt)
                break
            else:
                queue.popleft()
        # 최대값이 아니면 회전
        else:
            queue.rotate(-1)

for i in rst:
    print(i)