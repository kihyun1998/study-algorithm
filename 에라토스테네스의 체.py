# 1부터 1000까지 소수 검사
n=1000
primes=[]

# 0과 1을 제외한 모두 True로 만들기
beforePrimes = [False,False]+[True]*(n-1)

for i in range(2,n+1):
    # 소수의 배수로 걸러지지 않았다면
    if beforePrimes[i]:
        # 소수 리스트에 추가
        primes.append(i)
        # 추가한 소수의 배수들을 False
        for j in range(2*i,n+1,i):
            beforePrimes[j]=False
print(primes)

