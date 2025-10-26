from itertools import chain

print("=== chain은 iterator다! ===\n")

# chain 객체 생성
str1 = "abc"
str2 = "def"
chained = chain.from_iterable(zip(str1, str2))

print(f"chain 객체: {chained}")
print(f"타입: {type(chained)}\n")

# 1. for문으로 바로 사용 가능
print("1. for문으로 순회:")
chained = chain.from_iterable(zip(str1, str2))
for char in chained:
    print(f"  {char}", end=" ")
print("\n")

# 2. list()로 변환
print("2. list로 변환:")
chained = chain.from_iterable(zip(str1, str2))
result = list(chained)
print(f"  {result}\n")

# 3. next()로 하나씩 꺼내기
print("3. next()로 하나씩:")
chained = chain.from_iterable(zip(str1, str2))
print(f"  첫번째: {next(chained)}")
print(f"  두번째: {next(chained)}")
print(f"  세번째: {next(chained)}")
print(f"  나머지: {list(chained)}\n")

# 4. 다른 처리가 필요할 때
print("=== 다른 처리가 필요할 때 ===\n")

# 방법 1: for문에서 직접 처리
print("방법 1: for문에서 직접 처리")
chained = chain.from_iterable(zip(str1, str2))
result = []
for char in chained:
    # 대문자로 변환 + 느낌표 추가
    processed = char.upper() + "!"
    result.append(processed)
print(f"  {result}")
print(f"  합치기: {''.join(result)}\n")

# 방법 2: map 함수 사용 (추천!)
print("방법 2: map 함수 사용")
chained = chain.from_iterable(zip(str1, str2))
result = map(lambda x: x.upper() + "!", chained)
print(f"  map 객체: {result}")
print(f"  결과: {''.join(result)}\n")

# 방법 3: 함수 정의해서 사용
print("방법 3: 함수 정의")
def process_char(char):
    """문자를 처리하는 함수"""
    return f"[{char.upper()}]"

chained = chain.from_iterable(zip(str1, str2))
result = map(process_char, chained)
print(f"  결과: {''.join(result)}\n")

# 방법 4: 제너레이터 표현식
print("방법 4: 제너레이터 표현식")
chained = chain.from_iterable(zip(str1, str2))
result = (char.upper() + "!" for char in chained)
print(f"  제너레이터: {result}")
print(f"  결과: {''.join(result)}\n")

# 실전 예시들
print("\n=== 실전 예시 ===\n")

# 예시 1: 숫자 처리
print("1. 숫자 리스트 펼치고 2배로 만들기:")
numbers = [[1, 2], [3, 4], [5, 6]]
doubled = map(lambda x: x * 2, chain.from_iterable(numbers))
print(f"  원본: {numbers}")
print(f"  결과: {list(doubled)}\n")

# 예시 2: 필터링 추가
print("2. 펼치고 필터링:")
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
chained = chain.from_iterable(numbers)
# 짝수만
evens = filter(lambda x: x % 2 == 0, chained)
print(f"  원본: {numbers}")
print(f"  짝수만: {list(evens)}\n")

# 예시 3: 복잡한 처리
print("3. 문자열 섞고 복잡하게 처리:")
def complex_process(char):
    """복잡한 처리 함수"""
    if char.islower():
        return char.upper() + "!"
    else:
        return char.lower() + "?"

str1 = "abc"
str2 = "DEF"
chained = chain.from_iterable(zip(str1, str2))
result = map(complex_process, chained)
print(f"  str1: {str1}")
print(f"  str2: {str2}")
print(f"  결과: {''.join(result)}\n")

# 예시 4: chain -> filter -> map 조합
print("4. chain -> filter -> map 파이프라인:")
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
result = map(
    lambda x: x ** 2,  # 제곱
    filter(
        lambda x: x % 2 == 0,  # 짝수만
        chain.from_iterable(numbers)  # 펼치기
    )
)
print(f"  원본: {numbers}")
print(f"  짝수의 제곱: {list(result)}\n")

# 예시 5: 여러 처리를 함수로 분리
print("5. 여러 단계 처리를 함수로:")

def flatten(nested_list):
    """2D 리스트를 1D로"""
    return chain.from_iterable(nested_list)

def filter_evens(numbers):
    """짝수만 필터링"""
    return filter(lambda x: x % 2 == 0, numbers)

def square_all(numbers):
    """모두 제곱"""
    return map(lambda x: x ** 2, numbers)

# 파이프라인 구성
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = square_all(filter_evens(flatten(numbers)))
print(f"  원본: {numbers}")
print(f"  결과: {list(result)}\n")

# 성능 비교
print("\n=== 성능: chain + map vs 일반 for문 ===\n")

import time

n = 100000
data = [["a", "b"], ["c", "d"]] * (n // 4)

# 방법 1: for문
start = time.time()
result1 = []
for pair in data:
    for char in pair:
        result1.append(char.upper())
final1 = ''.join(result1)
time1 = time.time() - start

# 방법 2: chain + map
start = time.time()
final2 = ''.join(map(str.upper, chain.from_iterable(data)))
time2 = time.time() - start

print(f"데이터 크기: {n}개")
print(f"for문:      {time1:.4f}초")
print(f"chain+map:  {time2:.4f}초")
print(f"속도 차이:  {time1/time2:.2f}배 빠름")
print(f"결과 동일:  {final1 == final2}")

print("\n\n=== 핵심 정리 ===\n")
print("chain은 iterator이므로:")
print("1. for문으로 직접 순회 가능")
print("2. map()으로 각 요소 변환 가능")
print("3. filter()로 필터링 가능")
print("4. 제너레이터 표현식 사용 가능")
print("5. 함수 정의해서 처리 가능")
print("\n모두 조합해서 파이프라인 구성 가능!")
print("예: ''.join(map(process, filter(condition, chain(...))))")
