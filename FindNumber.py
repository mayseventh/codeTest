def solution(num, k):
    answer = 0

    temp = str(num)

    print(temp.find(str(k)))

    if temp.find(str(k)) >= 0:
        answer = temp.index(str(k))+1
    else:
        answer = -1
    
    return answer

print(solution(29183, 1))
print(solution(232443, 4))
print(solution(123456, 7))