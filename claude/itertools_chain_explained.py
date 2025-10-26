from itertools import chain

print("=== itertools.chain 기본 개념 ===\n")

# 1. chain의 기본 동작: 여러 iterable을 하나로 연결
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

result = chain(list1, list2, list3)
print(f"chain({list1}, {list2}, {list3})")
print(f"결과: {list(result)}")
print()

# 2. chain.from_iterable: iterable의 iterable을 펼침
nested = [[1, 2], [3, 4], [5, 6]]
print(f"원본 (중첩 리스트): {nested}")
print(f"chain.from_iterable 결과: {list(chain.from_iterable(nested))}")
print()

# 3. zip과 chain.from_iterable을 함께 사용
str1 = "abc"
str2 = "def"

print("=== zip과 chain 조합 ===\n")
print(f"str1 = '{str1}'")
print(f"str2 = '{str2}'")
print()

# 단계별 과정
zipped = list(zip(str1, str2))
print(f"1단계 - zip(str1, str2): {zipped}")
print(f"   -> 각 문자를 튜플로 묶음")
print()

chained = list(chain.from_iterable(zip(str1, str2)))
print(f"2단계 - chain.from_iterable: {chained}")
print(f"   -> 튜플들을 하나씩 펼침")
print()

result = ''.join(chain.from_iterable(zip(str1, str2)))
print(f"3단계 - join: '{result}'")
print(f"   -> 하나의 문자열로 합침")
print()

print("\n=== 다른 예시들 ===\n")

# 예시 1: 2D 리스트를 1D로 펼치기
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = list(chain.from_iterable(matrix))
print(f"2D -> 1D 변환:")
print(f"원본: {matrix}")
print(f"결과: {flat}")
print()

# 예시 2: 여러 문자열 합치기
words = ["hello", "world", "python"]
chars = list(chain.from_iterable(words))
print(f"여러 문자열 -> 문자 리스트:")
print(f"원본: {words}")
print(f"결과: {chars}")
print(f"다시 합침: {''.join(chars)}")
print()

# 예시 3: chain vs chain.from_iterable 차이
print("=== chain vs chain.from_iterable 차이 ===\n")

a = [1, 2]
b = [3, 4]
c = [5, 6]

# chain: 인자를 직접 나열
result1 = list(chain(a, b, c))
print(f"chain(a, b, c): {result1}")

# chain.from_iterable: iterable 하나를 받음
iterable_of_iterables = [a, b, c]
result2 = list(chain.from_iterable(iterable_of_iterables))
print(f"chain.from_iterable([a, b, c]): {result2}")
print()

# 예시 4: 왜 빠른가?
print("=== 왜 chain이 빠를까? ===\n")

# 방법 1: 수동으로 append (느림)
def manual_way(str1, str2):
    result = []
    for c1, c2 in zip(str1, str2):
        result.append(c1)  # append 2번 호출
        result.append(c2)
    return ''.join(result)

# 방법 2: chain 사용 (빠름)
def chain_way(str1, str2):
    return ''.join(chain.from_iterable(zip(str1, str2)))

print("방법 1 (수동):")
print("  - append를 n*2번 호출")
print("  - 파이썬 레벨에서 반복문 실행")
print()
print("방법 2 (chain):")
print("  - C로 작성된 최적화된 iterator")
print("  - 메모리 효율적 (lazy evaluation)")
print("  - join이 직접 iterator를 소비")
print()

# 예시 5: chain의 lazy evaluation (게으른 평가)
print("=== Lazy Evaluation (게으른 평가) ===\n")

def print_and_yield(name, items):
    """값을 yield할 때만 출력"""
    for item in items:
        print(f"  {name}에서 {item} 생성")
        yield item

# chain은 실제로 필요할 때만 값을 가져옴
print("chain 생성 (아직 실행 안 됨):")
lazy_chain = chain(
    print_and_yield("A", [1, 2]),
    print_and_yield("B", [3, 4])
)
print(f"  chain 객체: {lazy_chain}")
print()

print("실제로 값을 사용할 때:")
result = list(lazy_chain)
print(f"  결과: {result}")
