def solution(str1, str2):
    answer = 2

    print("len(str1), len(str2) : {0}, {1}".format(len(str1), len(str2)))
    
    for i in range (len(str1)):
        print("i, len(str2), str[i:len(str2) : {0}, {1}, {2}]".format(i, len(str2), str1[i:len(str2)]))
        if str1[i:i+len(str2)] == str2:
            answer = 1
            
    return answer

print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))