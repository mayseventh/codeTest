def solution(my_string):
    answer = 0
    i, check = 0,0

    num_list = []
    print(len(my_string))

    while i < len(my_string):
        print("i is : {0}".format(i))
        if my_string[i].isdigit():
            if i+1 < len(my_string):
                for j in range (i+1, len(my_string)):
                    print("j, my_string[j] : {0}, {1}".format(j, my_string[j]))
                    if my_string[j].isalpha():
                        check = j
                        print("check is : {0}".format(check))
                        break;
                    else:
                        check = j+1
                print(my_string[i:check])
                num_list.append(my_string[i:check])
            elif i+1 == len(my_string):
                check = i+1
                num_list.append(my_string[i:check])
        if check > 0:
            i = check
        else :
            i += 1

        check = 0

    # print(num_list)

    print(num_list)
    for i in num_list:
        answer += int(i)

    return answer

# print(solution("1a2b3c4d123Z"))
# print(solution("a1bc1000dZ"))
print(solution("a1"))