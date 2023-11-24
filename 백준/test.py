s1 = int(input())
s2 = list(map(int, input().split()))

cnt =0
for i in s2:
    if i % 2 == 0: cnt+=1
    else: cnt-=1


if cnt>0:
    print("Happy")
else:
    print("Sad")