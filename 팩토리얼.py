def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

# 4!에 대한 예시
print(factorial(4))