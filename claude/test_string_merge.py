import time

# 원본 코드
def solution_original(str1, str2):
    answer = []
    for i in range(len(str1)*2):
        if i % 2 == 0:
            if(i==0):
                answer.append(str1[i])
            else:
                index = i // 2
                answer.append(str1[index])
        else:
            j = i -1
            if(j == 0):
                answer.append(str2[j])
            else:
                index = j // 2
                answer.append(str2[index])
    return ''.join(answer)

# 개선 1: 로직 단순화
def solution_v1(str1, str2):
    answer = []
    for i in range(len(str1)*2):
        if i % 2 == 0:
            answer.append(str1[i // 2])
        else:
            answer.append(str2[i // 2])
    return ''.join(answer)

# 개선 2: zip 사용 (가장 파이썬스러움)
def solution_v2(str1, str2):
    answer = []
    for c1, c2 in zip(str1, str2):
        answer.append(c1)
        answer.append(c2)
    return ''.join(answer)

# 개선 3: 리스트 컴프리헨션 + zip
def solution_v3(str1, str2):
    return ''.join(c for pair in zip(str1, str2) for c in pair)

# 개선 4: itertools (메모리 효율적)
from itertools import chain
def solution_v4(str1, str2):
    return ''.join(chain.from_iterable(zip(str1, str2)))


# 테스트
str1 = "abc"
str2 = "def"

print("=== 결과 확인 ===")
print(f"원본: {solution_original(str1, str2)}")
print(f"v1:   {solution_v1(str1, str2)}")
print(f"v2:   {solution_v2(str1, str2)}")
print(f"v3:   {solution_v3(str1, str2)}")
print(f"v4:   {solution_v4(str1, str2)}")

# 성능 테스트
str1_large = "a" * 10000
str2_large = "b" * 10000
n = 1000

print(f"\n=== 성능 비교 (길이 {len(str1_large)}, {n}회 반복) ===")

start = time.time()
for _ in range(n):
    solution_original(str1_large, str2_large)
time1 = time.time() - start
print(f"원본:       {time1:.4f}초")

start = time.time()
for _ in range(n):
    solution_v1(str1_large, str2_large)
time2 = time.time() - start
print(f"v1 (단순화): {time2:.4f}초 ({time1/time2:.2f}배)")

start = time.time()
for _ in range(n):
    solution_v2(str1_large, str2_large)
time3 = time.time() - start
print(f"v2 (zip):   {time3:.4f}초 ({time1/time3:.2f}배)")

start = time.time()
for _ in range(n):
    solution_v3(str1_large, str2_large)
time4 = time.time() - start
print(f"v3 (컴프):   {time4:.4f}초 ({time1/time4:.2f}배)")

start = time.time()
for _ in range(n):
    solution_v4(str1_large, str2_large)
time5 = time.time() - start
print(f"v4 (chain): {time5:.4f}초 ({time1/time5:.2f}배)")
