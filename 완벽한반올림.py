# 일반 반올림과의 차이는 
# 이것을 추가한다는 점 >10 ** ( -len(str(val))-1 )

# 이를 추가함으로 파이썬의 round문제를 해결해줌

def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)