from pprint import pprint

def solution(numlist, n):
    answer = []
    index_list = []
    
    for i in numlist:
        temp = abs(i - n)
        index_list.append([temp, i])
    
    index_list.sort(key=lambda x:(x[0], -x[1]))    
    pprint(index_list)
    
    for x in index_list:
        answer.append(x[1])
            
    return answer

print(solution([1, 2, 3, 4, 5, 6], 4))