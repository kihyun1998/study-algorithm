def solution(my_string, overwrite_string, s):
    str_list = list(my_string)
    print(str_list)
    overstr_list = list(overwrite_string)

    print(overstr_list)
    str_list[s:s+len(overstr_list)] = overstr_list
    print(str_list)
    
    return ''.join(str_list)

s = solution("He11oWor1d","lloWorl",2)
print(s)