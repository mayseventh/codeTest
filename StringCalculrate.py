def solution(my_string):
    answer = 0
    
    cal = my_string.split(" ")

    answer = int(cal[0])

    for i in range(1, len(cal)):
        if cal[i] == "+":
            answer += int(cal[i+1])
        elif cal[i] == "-":
            answer -= int(cal[i+1])
        
    return answer

print(solution("3 + 4 - 1"))
