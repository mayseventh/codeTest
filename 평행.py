def solution(dots):
    answer = 0
    
    dots.sort()
    print(dots)
    
    # 첫번째-두번째, 세번째-네번째 연결선
    if (dots[1][1]-dots[0][1])/(dots[1][0]-dots[0][0]) == (dots[3][1]-dots[2][1])/(dots[3][0]-dots[2][0]):
        answer = 1
    # 첫번째-세번째, 두번째-네번째 연결선    
    elif (dots[2][1]-dots[0][1])/(dots[2][0]-dots[0][0]) == (dots[3][1]-dots[1][1])/(dots[3][0]-dots[1][0]):
        answer = 1
    # 첫번째-네번째, 두번째-세번째 연결선
    elif (dots[3][1]-dots[0][1])/(dots[3][0]-dots[0][0]) == (dots[2][1]-dots[1][1])/(dots[2][0]-dots[1][0]):
        answer = 1
    else:
        answer = 0
    
    return answer

# print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))

# print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))

print(solution([[2,6], [4,4], [8,8], [10,14]]))