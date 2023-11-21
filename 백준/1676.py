def factorial(num):
    if num==0:
        return 1
    return  num * factorial(num-1)

n = int(input())

nFactorial = reversed(str(factorial(n)))

for i,v in enumerate(nFactorial):
    if v != '0':
        print(i)
        break
else:
    print(len(nFactorial))