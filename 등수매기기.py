def solution(score):
    answer = []
    
    # average = list(set(map(lambda x:(x[0]+x[1])//2, score)))
    # average.sort(reverse=True)
    
    # for i in range(len(average)):
    #     aver_dic[average[i]] = i+1
        
    # print(aver_dic)
    
    # for x in score:
    #     answer.append(aver_dic[(x[0]+x[1])//2])
    
    
    average = list(map(lambda x:(x[0]+x[1])//2, score))
    # print(average)
    
    for i in range(len(score)):
        cnt = 1
        for j in range(len(score)):
            if i != j and sum(score[i]) < sum(score[j]):
                # print("aver[i], aver[j] : {0}, {1}".format(sum(score[i]), sum(score[j])))
                cnt += 1
        
        # print("cnt is : {0}".format(cnt))
        answer.append(cnt)
    
    return answer

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
print(solution([[1, 3], [3, 1], [2, 3], [3, 2], [1, 2], [0, 0]])) # [3, 3, 1, 1, 5, 6]