def solution(s):
    answer = 0
    check = 0
    i_list = s.split()
    
    print(i_list)
    
    for i in i_list:
        if i == 'Z':
            answer -= check
            print("zzzzz i, check, ansser : {0}, {1}, {2}".format(i, check, answer))
        else :
            check = int(i)
            answer += check
            print("i, check, ansser : {0}, {1}, {2}".format(i, check, answer))
                
    return answer

print(solution("10 Z 20 Z 1"))