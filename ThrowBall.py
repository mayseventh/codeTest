def solution(numbers, k):
    answer = 0
    temp = 1
    
    for i in range (1, k):
        if temp+2 < len(numbers):
            print(("<, i, i+2, number[i+1] : {0}, {1}, {2}".format(i, i+2, numbers[temp+1])))
            answer = numbers[temp+1]
        elif temp+2 > len(numbers):
            print((">, i, i+2, number[(i+2)%len(numbers)-1] : {0}, {1}, {2}".format(i, i+2, numbers[(temp+2)%len(numbers)-1])))
            answer = numbers[(temp+2)%len(numbers)-1]   
        temp += 2   
    
    return answer

print(solution([1, 2, 3, 4, 5, 6], 5))