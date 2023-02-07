def solution(n):
    answer = 0
    if 0 < n <= 7:
        answer = 1
    
    else :
        if n % 7 == 0:
            answer = n//7
        else :
            answer = (n//7)+1
           
    return answer

print(solution(21))