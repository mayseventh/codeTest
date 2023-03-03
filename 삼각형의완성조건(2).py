def solution(sides):
    answer = 0
    
    sides.sort()
    
    # sides의 max값이 가장 긴 변인 경우
    for i in range(1, sides[1]+1):
        if i+sides[0] > sides[1] :
            print("i, sides[0], sides[1] is : {0}, {1}, {2}".format(i, sides[0], sides[1]))
            answer += 1
    
    # 나머지 한 변이 가장 긴 변인 경우
    for j in range(sides[1]+1, sides[0]+sides[1]):
        if sides[0]+sides[1] > j:
            print("j, sides[0], sides[1] is : {0}, {1}, {2}".format(j, sides[0], sides[1]))
            answer += 1
    
    return answer

print(solution([11, 7]))