init_a,init_b = map(int,input().split())

a,b = init_a,init_b

while(True):
    if a > b:
        if a%b==0:
            print(b)
            print(init_a*init_b // b)
            break
        else:
            a %= b
    else:
        if b%a==0:
            print(a)
            print(init_a*init_b // a)
            break
        else:
            b %= a
