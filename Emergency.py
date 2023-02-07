def solution(emergency):
    answer = []
    
    order = {}
    temp = []

    
    for i in emergency:
        temp.append(i)

    temp.sort(reverse=True)
    for i in range(len(temp)):
        order[temp[i]] = i+1


    for j in emergency:
        answer.append(order[j])

    return answer

print(solution([3, 76, 24]))