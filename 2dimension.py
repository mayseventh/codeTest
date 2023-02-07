def solution(num_list, n):
    answer = []
    
    for i in range (0,len(num_list),n):
        print("i, , n, num_list[i::n] : {0}, {1}, {2}".format(i, n, num_list[i:n+i]))
        answer.append(num_list[i:n+i])
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))