def solution(array):
    answer = []

    print(max(array))
    print(array.index(max(array)))

    answer.append(max(array))
    answer.append(array.index(max(array)))

    return answer

print(solution([9, 10, 11, 8]))