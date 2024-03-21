import sys

N,K = map(int, sys.stdin.readline().rstrip().split())

temp_lst = list(map(int, sys.stdin.readline().rstrip().split()))

temp_sum = sum(temp_lst[:K])
answer = temp_sum

for i in range(N-K):
    temp_sum += temp_lst[i+K] - temp_lst[i]
    if answer < temp_sum:
        answer = temp_sum
print(answer)