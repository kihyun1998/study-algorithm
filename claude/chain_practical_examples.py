from itertools import chain

print("=== chain으로 다른 처리하는 실전 예시 ===\n")

# 예시 1: 문자열 섞으면서 특정 처리
print("1. 문자열 섞으면서 인덱스 붙이기:")
str1 = "abc"
str2 = "def"

# for문으로
result = []
for i, char in enumerate(chain.from_iterable(zip(str1, str2))):
    result.append(f"{i}:{char}")
print(f"  결과: {', '.join(result)}\n")

# 예시 2: 조건부 처리
print("2. 짝수 인덱스만 대문자로:")
chained = chain.from_iterable(zip(str1, str2))
result = []
for i, char in enumerate(chained):
    if i % 2 == 0:
        result.append(char.upper())
    else:
        result.append(char)
print(f"  결과: {''.join(result)}\n")

# 예시 3: map으로 함수 적용
print("3. 각 문자마다 다른 함수 적용:")

def process_alternating(item):
    """튜플 (인덱스, 값)을 받아서 처리"""
    i, char = item
    if i % 2 == 0:
        return char.upper()
    else:
        return char.lower()

chained = chain.from_iterable(zip(str1, str2))
result = map(process_alternating, enumerate(chained))
print(f"  결과: {''.join(result)}\n")

# 예시 4: 실전 - 2D 배열 처리
print("4. 2D 배열 펼쳐서 양수만 필터링하고 제곱:")
matrix = [[1, -2, 3], [-4, 5, 6], [7, -8, 9]]

# chain으로 펼치고 -> filter로 양수만 -> map으로 제곱
result = list(
    map(lambda x: x ** 2,
        filter(lambda x: x > 0,
               chain.from_iterable(matrix)))
)
print(f"  원본: {matrix}")
print(f"  결과: {result}\n")

# 예시 5: 여러 리스트를 펼치면서 변환
print("5. 여러 파일명을 합치고 확장자 추가:")
files_group1 = ["file1", "file2"]
files_group2 = ["file3", "file4"]
files_group3 = ["file5"]

# chain으로 합치고 map으로 .txt 추가
all_files = map(lambda f: f + ".txt", chain(files_group1, files_group2, files_group3))
print(f"  결과: {list(all_files)}\n")

# 예시 6: 복잡한 데이터 구조 처리
print("6. 학생별 점수 펼치고 평균 구하기:")
students_scores = [
    [85, 90, 88],  # 학생1
    [92, 88, 95],  # 학생2
    [78, 85, 82],  # 학생3
]

all_scores = list(chain.from_iterable(students_scores))
average = sum(all_scores) / len(all_scores)
print(f"  모든 점수: {all_scores}")
print(f"  전체 평균: {average:.2f}\n")

# 예시 7: 함수 체이닝
print("7. 여러 단계 처리를 함수로 조합:")

def flatten_2d(matrix):
    """2D -> 1D"""
    return chain.from_iterable(matrix)

def keep_positive(numbers):
    """양수만"""
    return filter(lambda x: x > 0, numbers)

def square(numbers):
    """제곱"""
    return map(lambda x: x ** 2, numbers)

def sum_all(numbers):
    """합계"""
    return sum(numbers)

# 파이프라인
matrix = [[1, -2, 3], [-4, 5], [6, -7, 8, 9]]
result = sum_all(square(keep_positive(flatten_2d(matrix))))
print(f"  원본: {matrix}")
print(f"  양수의 제곱 합: {result}")
print(f"  계산: 1^2 + 3^2 + 5^2 + 6^2 + 8^2 + 9^2 = {1+9+25+36+64+81}\n")

# 예시 8: 실용적인 패턴 - 데이터 클리닝
print("8. 여러 CSV 행을 펼치고 공백 제거:")
csv_rows = [
    ["  apple ", " banana "],
    [" orange", "grape  "],
    ["  kiwi  "],
]

# 펼치고 -> strip 적용 -> 다시 합치기
cleaned = list(map(str.strip, chain.from_iterable(csv_rows)))
print(f"  원본: {csv_rows}")
print(f"  정제: {cleaned}\n")

# 예시 9: 커스텀 처리 함수
print("9. 문자열 섞으면서 암호화:")

def custom_encode(char, position):
    """위치에 따라 다르게 인코딩"""
    offset = position % 3
    return chr(ord(char) + offset)

str1 = "hello"
str2 = "world"

chained = chain.from_iterable(zip(str1, str2))
encoded = ''.join(custom_encode(char, i) for i, char in enumerate(chained))
print(f"  원본: '{str1}' + '{str2}'")
print(f"  섞음: {''.join(chain.from_iterable(zip(str1, str2)))}")
print(f"  암호: {encoded}\n")

# 예시 10: 실전 - 로그 파일 처리 시뮬레이션
print("10. 여러 로그 파일의 에러만 추출:")

log1 = ["INFO: started", "ERROR: failed", "INFO: ok"]
log2 = ["ERROR: timeout", "INFO: success"]
log3 = ["INFO: done", "ERROR: crash", "ERROR: bug"]

# 모든 로그를 펼치고 -> ERROR만 필터링 -> 에러 메시지만 추출
all_logs = chain(log1, log2, log3)
errors_only = filter(lambda line: line.startswith("ERROR"), all_logs)
error_messages = map(lambda line: line.replace("ERROR: ", ""), errors_only)

print(f"  에러 목록:")
for err in error_messages:
    print(f"    - {err}")

print("\n\n=== 핵심 정리 ===\n")
print("chain + 다른 처리 조합:")
print()
print("1. chain + for문:")
print("   for item in chain.from_iterable(data):")
print("       # 직접 처리")
print()
print("2. chain + map (변환):")
print("   map(function, chain.from_iterable(data))")
print()
print("3. chain + filter (필터링):")
print("   filter(condition, chain.from_iterable(data))")
print()
print("4. chain + enumerate (인덱스):")
print("   enumerate(chain.from_iterable(data))")
print()
print("5. 조합:")
print("   map(f2, filter(f1, chain.from_iterable(data)))")
print()
print("핵심: chain은 iterator니까 iterator를 받는 모든 함수/문법과 사용 가능!")
