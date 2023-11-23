n = int(input())
cnt=0
while n!=1:

    if n % 3 == 0:
        n /= 3
    elif n % 2 == 0:
        n /= 2
    else:
        n -= 1

    if n==1:
        print(cnt)
        break
    else:
        cnt+=1
else:
    print(cnt)
    