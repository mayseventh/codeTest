def solution(a, b):
    answer = 0
    
    # 최eo공약수로 기약분수 처리
    for i in range(min(a,b), 0, -1):
        if a%i == 0 and b%i == 0:
            gcd = i
            break
    
    divide = b//gcd
    
    # 소인수분해
    temp = []
    x = 2
    while x <= divide:
        if divide%x == 0:
            divide = divide / x
            temp.append(x)
        else:
            x += 1
    
    # 유한소수 판별
    if len(temp) == 0:
        answer = 1
    else:
        for j in temp:
            if j not in ([2,5]):
                answer = 2
                break
            else:
                answer = 1
    
    return answer

# print(solution(7,20))
# print(solution(11,22))
# print(solution(12,21))
# print(solution(3500, 500))
print(solution(7,30))