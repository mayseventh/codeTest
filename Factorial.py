def nfactorial (arg):
    facto = 1
    for i in range (arg, 0, -1):
        print(i, arg, facto)
        facto *= i
    
    print("facto is : {0}".format(facto))
    return facto

def solution(balls, share):
    answer = 0
    
    answer = nfactorial(balls) / (nfactorial(balls-share) * nfactorial(share))
    return answer

print(solution(5, 3))