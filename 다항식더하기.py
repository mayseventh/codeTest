def solution(polynomial):
    answer = ''
    temp = polynomial.split(" ")

    x_list = []
    num_list = []

    if temp[0].find('x') >= 0:
        x_list.append(temp[0])
    else:
        num_list.append(temp[0])

    for i in range(1, len(temp)):
        if temp[i].find("x") >= 0:
            x_list.append(temp[i-1])
            x_list.append(temp[i])
        elif temp[i].isdigit():
            num_list.append(temp[i-1])
            num_list.append(temp[i])

    x_sum = x_list[0]
    y_sum = 0

    for i in range(1, len(x_list)):
        if x_list[i] == "+":
            if x_list[i+1].find("x") > 0:
                x_sum = str(int(x_sum[0])+x_list[i+1][0]) + 'x'
            else :
                if x_sum.find('x') > 0:
                    x_sum = str(int(x_sum[0])+1) + 'x'
                else :
                    x_sum = '2x'
        elif x_list[i] == "-":
            if x_list[i+1].find("x") > 0:
                x_sum = str(int(x_sum[0])-x_list[i+1][0]) + 'x'
            else :
                if x_sum.find('x') > 0:
                    x_sum = str(int(x_sum[0])-1) + 'x'
                else :
                    x_sum = ''

    if len(num_list) != 0:
        y_sum = eval(''.join(num_list))   

    if y_sum > 0 :
        answer = x_sum + '+' + str(y_sum)
    elif y_sum < 0 :
        answer = x_sum + '-' + str(y_sum)
    else :
        answer = x_sum

    return answer

# print(solution("3x + 7 + x"))
print(solution("x + x + x"))