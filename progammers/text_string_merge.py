def solution(str1, str2):
    answer = []
    # str1과 str2는 길이가 같으니 len(str1)*2로 효율적으로 구함
    for i in range(len(str1)*2):
        # 짝수라면 str1에서
        # 0,2,4,8
        if i % 2 == 0:
            if(i==0):
                answer.append(str1[i])
            else:
                index = i // 2
                answer.append(str1[index])
        
        # 홀수라면 str2에서
        # 1,3,5,7
        else:
            j = i -1
            if(j == 0):
                answer.append(str2[j])
            else:
                index = j // 2
                answer.append(str2[index])
    
    return ''.join(answer)