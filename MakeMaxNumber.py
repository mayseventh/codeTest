def solution(numbers):
    answer = -1000000000
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i]*numbers[j] >= answer :
                answer = numbers[i]*numbers[j]
                
    return answer

print(solution([10, 20, 30, 5, 5, 20, 5]))
# print(solution([-8,2,3]))
# print(solution([-10000, 10000]))