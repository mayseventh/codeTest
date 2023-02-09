def solution(n):
    answer = []
    d_list = []
    
    i = 2
    
    while i <= n:
        if n%i == 0:
            d_list.append(i)
            n /= i
        else:
            i += 1
            
    answer = (list(set(d_list)))
    answer.sort()
            
    return answer

print(solution(420))