def solution(numbers, direction):
    answer = []
    
    if direction == "right":
        answer.append(numbers[len(numbers)-1])
        for i in numbers[0:len(numbers)-1]:
            answer.append(i)
    elif direction == "left":
        for i in numbers[1:len(numbers)-1]:
            answer.append(i)
        answer.append(numbers[0])
        
    return answer

print(solution([4, 455, 6, 4, -1, 45, 6], "left"))