def solution(my_string):
    answer = 0

    for i in range (10):
        answer += (i*my_string.count(str(i)))
    
    return answer

print(solution("aAb1B2cC34oOp"))