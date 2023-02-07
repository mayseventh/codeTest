def solution(my_string):
    answer = ''

    cnt = len(my_string)-1

    for i in range (len(my_string)):
        answer += my_string[cnt-i]

    return answer

print(solution("jaron"))