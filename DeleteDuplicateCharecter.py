def solution(my_string):
    answer = ''
    c_list = list(my_string)
    
    print(c_list)
    
    for i in c_list:
        if answer.count(i):
            pass
        else:
            answer += i
        
    return answer

print(solution("We are the world"))