def solution(cipher, code):
    answer = ''
    
    for i in range (0, len(cipher)+1, code):
        if code == 1 :
            answer = cipher
        elif 0 < i <= code :
            print("code, i, cipher[i] : {0}, {1}, {2}".format(code, i, cipher[i]))
            answer += cipher[i-1]
        elif i > code :
            answer += cipher[i-1]

    return answer

print(solution("dfjardstddetckdaccccdegk", 4))