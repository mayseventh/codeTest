def nfactorial (arg):
    facto = 1
    for i in range (arg, 0, -1):
        print(i, arg, facto)
        facto *= i
    
    print("facto is : {0}".format(facto))
    return facto

def solution(n):
    answer = 0
    
    for i in range (1, n+1):
        if nfactorial(i) > n:
            break
        else:
            answer += 1
            
    return answer

print(solution(1))