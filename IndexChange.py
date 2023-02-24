def solution(my_string, num1, num2):
    answer = list(my_string)

    answer[num1] = my_string[num2]
    answer[num2] = my_string[num1]

    # answer = answer.replace(answer[num1], my_string[2], 1)
    # print(answer)
    # answer = answer.replace(answer[num2], my_string[1], 1)
    print(''.join(answer))
    return ''.join(answer)

print(solution("hello", 1, 2))