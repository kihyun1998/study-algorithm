
# 값 입력
m,n = map(int, input().split())
arr_case = [list(map(int, input().split())) for _ in range(n)]


mList = [0 for i in range(m)]

for case in arr_case:
    for i in range(case[0],case[1]+1):
        mList[i-1] = case[2]

for i in mList:
    print(i,end=" ")