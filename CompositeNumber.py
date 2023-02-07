def solution(n):
    answer = 0
    
    count = 0
    for i in range (1, n+1):
        for j in range(1, i+1):
            if i%j==0:
                print("i, j : {0}, {1}".format(i, j))
                count += 1
        
        if count >=3 :
            print("i, count : {0}, {1}".format(i, count))
            answer += 1
            
        count = 0
            
    return answer

print(solution(10))