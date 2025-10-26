import time

# 테스트 데이터 크기
n = 10000

# 방법 1: str += (느림)
start = time.time()
result1 = ""
for i in range(n):
    result1 += str(i)
time1 = time.time() - start

# 방법 2: list + join (빠름)
start = time.time()
result2 = []
for i in range(n):
    result2.append(str(i))
result2 = ''.join(result2)
time2 = time.time() - start

print(f"=== {n}개의 문자열 연결 성능 비교 ===\n")
print(f"str += 방식: {time1:.4f}초")
print(f"list + join 방식: {time2:.4f}초")
print(f"\n속도 차이: {time1/time2:.2f}배 빠름")
print(f"\n결과 동일: {result1 == result2}")
