def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        answer += 1
        print("i, answer is : {0}, {1}".format(i, answer))
        while answer > 0:            
            if answer%3 != 0 and str(answer).find('3') < 0:
                break
                print("3x case answer is : {0}".format(answer))
            answer += 1
            print("3x****** case i, answer is : {0}, {1}".format(i, answer))
            
    return answer

print(solution(40))