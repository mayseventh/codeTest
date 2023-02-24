def solution(dots):
    answer = 0
    x_list, y_list = [], []
    
    for i in dots:
        x_list.append(i[0])
        y_list.append(i[1])
    
    x_list.sort()
    y_list.sort()
    print(x_list)
    print(y_list)
    
    answer = (x_list[3] - x_list[0])*(y_list[3]-y_list[0])/2
    
    return answer

print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))