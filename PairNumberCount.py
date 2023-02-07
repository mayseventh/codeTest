def solution(n):
    answer = 0
    temp = n+1
    
    for i in range (1, n+1):
        if i*(temp-i) == n:
            answer += 1
            print("i, temp-i, answer : {0}, {1}, {2}".format(i, temp-i, answer))
                
    return answer

print(solution(20))