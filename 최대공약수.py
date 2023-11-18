a,b = map(int,input().split())

while(True):
    if a > b:
        if a%b==0:
            print(b)
            break
        else:
            a %= b
    else:
        if b%a==0:
            print(a)
            break
        else:
            b %= a
