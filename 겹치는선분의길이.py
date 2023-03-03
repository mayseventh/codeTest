def solution(lines):
    answer = 0
    max_num, min_num, check = 0, 0, 0
    
    lines.sort()
    
    for i in lines:
        if max_num < max(i):
            max_num = max(i)
            
        if min_num > min(i):
            min_num = min(i)
    
    print(min_num, max_num)

    
    for x in range(min_num, max_num+1):
        for block in lines:
            # print("x, min(block), max(block) : {0}, {1}, {2}".format(x, min(block), max(block)))
            if min(block) < x <= max(block):
                check += 1
                # print("x, block, check : {0}, {1}, {2}".format(x, block, check))
                
        if check >= 2:
            # print("x, block, check : {0}, {1}, {2}".format(x, block, check))
            answer += 1
        
        check = 0
    

    return answer

print(solution([[0, 5], [3, 9], [1, 10]]))

print(solution([[-1, 1], [1, 3], [3, 9]]))

print(solution([[0, 3], [-3, -1], [-2, 3]]))