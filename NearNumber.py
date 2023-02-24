def solution(array, n):
    answer = 0
    chk = n

    array.sort()

    for i in array:
        if i <= n:
            if n-i < chk:
                chk = n-i
                answer = i
        else:
            if i-n < chk:
                chk = i-n
                answer = i
    
    return answer

print(solution([5, 10, 20, 30], 20))
