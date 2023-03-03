def solution(polynomial):
    answer = ''
    temp = polynomial.split(" ")
    
    x_count = 0
    int_count = 0
    
    for i in temp:
        if i.find('x') == 0:
            # print("only x")
            x_count += 1
        elif i.find('x') > 0:
            # print("x + a")
            chk = i.replace('x', '')
            x_count += int(chk)
        elif i.isdigit():
            # print("digit")
            int_count += int(i)
    
    # print("x_count is : {0}".format(x_count))
    # print("int_count is : {0}".format(int_count))
    
    if x_count == 1:
        answer = 'x'
    else:
        answer = str(x_count) + 'x'
        
    if x_count != 0 and int_count != 0:
        answer += ' + ' + str(int_count)
    elif x_count == 0 and int_count != 0:
        answer = str(int_count)

    return answer

print(solution("3x + 7 + x"))
print(solution("x + x + 9x"))
print(solution("x + 4 + 7"))
print(solution("x"))