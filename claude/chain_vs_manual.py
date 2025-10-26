from itertools import chain
import time
import sys

print("=== chain이 빠른 이유 ===\n")

# 코드로 보는 차이점
str1 = "abc"
str2 = "def"

print("1. 수동 방식 (느림):")
print("""
answer = []
for c1, c2 in zip(str1, str2):
    answer.append(c1)  # ← 파이썬 함수 호출
    answer.append(c2)  # ← 파이썬 함수 호출
result = ''.join(answer)

문제점:
- append를 2n번 호출 (오버헤드)
- 파이썬 레벨 반복문 (느림)
- 명시적 리스트 생성 (메모리)
""")

print("\n2. chain 방식 (빠름):")
print("""
''.join(chain.from_iterable(zip(str1, str2)))

장점:
- C로 구현된 최적화된 iterator
- Lazy evaluation (필요할 때만 생성)
- join이 직접 iterator 소비 (중간 리스트 불필요)
- CPU 캐시 친화적
""")

# 실제 동작 확인
print("\n=== 실제 동작 과정 ===\n")

# zip 결과
zipped = zip(str1, str2)
print(f"zip('{str1}', '{str2}') 결과:")
for pair in zip(str1, str2):
    print(f"  {pair}")

print(f"\nchain.from_iterable로 펼치면:")
for char in chain.from_iterable(zip(str1, str2)):
    print(f"  '{char}'", end=" ")
print()

# 메모리 효율성 비교
print("\n\n=== 메모리 효율성 ===\n")

n = 1000000
str1_large = "a" * n
str2_large = "b" * n

# 방법 1: 리스트 생성
result = []
for c1, c2 in zip(str1_large, str2_large):
    result.append(c1)
    result.append(c2)
list_size = sys.getsizeof(result)
print(f"리스트 방식: {list_size:,} bytes")

# 방법 2: chain (iterator)
chain_obj = chain.from_iterable(zip(str1_large, str2_large))
chain_size = sys.getsizeof(chain_obj)
print(f"chain 방식:  {chain_size:,} bytes")
print(f"\n메모리 차이: {list_size // chain_size:,}배!")

# 성능 비교 (상세)
print("\n\n=== 상세 성능 비교 ===\n")

def method1_manual_append(s1, s2):
    """수동 append"""
    result = []
    for c1, c2 in zip(s1, s2):
        result.append(c1)
        result.append(c2)
    return ''.join(result)

def method2_extend(s1, s2):
    """extend 사용"""
    result = []
    for pair in zip(s1, s2):
        result.extend(pair)
    return ''.join(result)

def method3_comprehension(s1, s2):
    """리스트 컴프리헨션"""
    return ''.join([c for pair in zip(s1, s2) for c in pair])

def method4_generator(s1, s2):
    """제너레이터 표현식"""
    return ''.join(c for pair in zip(s1, s2) for c in pair)

def method5_chain(s1, s2):
    """chain.from_iterable"""
    return ''.join(chain.from_iterable(zip(s1, s2)))

n = 10000
test_str1 = "x" * n
test_str2 = "y" * n
iterations = 1000

methods = [
    ("수동 append", method1_manual_append),
    ("extend 사용", method2_extend),
    ("리스트 컴프", method3_comprehension),
    ("제너레이터", method4_generator),
    ("chain", method5_chain),
]

results = []
for name, func in methods:
    start = time.time()
    for _ in range(iterations):
        func(test_str1, test_str2)
    elapsed = time.time() - start
    results.append((name, elapsed))

# 가장 빠른 것 기준으로 정렬
results.sort(key=lambda x: x[1])

print(f"테스트: 길이 {n}, {iterations}회 반복\n")
fastest_time = results[0][1]

for i, (name, elapsed) in enumerate(results, 1):
    ratio = elapsed / fastest_time
    bar = "#" * int(ratio * 20)
    print(f"{i}. {name:15s}: {elapsed:.4f}sec  {bar}  ({ratio:.2f}x)")

print("\n\n=== 핵심 정리 ===\n")
print("chain.from_iterable이 빠른 이유:")
print("✓ C 레벨 최적화 (CPython)")
print("✓ 중간 리스트 생성 안 함 (메모리 절약)")
print("✓ Iterator protocol 사용 (효율적)")
print("✓ 함수 호출 오버헤드 최소화")
print("\n언제 사용?")
print("• 중첩된 iterable을 펼칠 때")
print("• 여러 시퀀스를 연결할 때")
print("• 메모리 효율이 중요할 때")
print("• 대용량 데이터 처리 시")
