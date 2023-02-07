def solution(num_list):
    answer = []
    
    even, odd = 0,0
    
    for i in num_list :
        print("i : {0}".format(i))
        if i%2 == 0:
            even += 1
            print("even : {0}".format(even))
        else :
            odd += 1
    
    answer.append(even)
    answer.append(odd)
    
    return answer

print(solution([1, 2, 3, 4, 5]))