

def solution(numer1, denom1, numer2, denom2):
    answer = []
    child = (numer1*denom2)+(numer2*denom1)
    parent = (denom1*denom2)
        
    answer = [child, parent]

    i = 2

    while i < parent-1 :
        print("i is {0}".format(i))
        if child%i == 0 and parent%i == 0:
            child = child//i
            parent = parent//i
            print("child is : {0}, parent is : {1}".format(child, parent))
            i = 2
        else :
            i += 1

    answer = [child, parent]
    return answer


# print(solution(1, 2, 3, 4))
# print(solution(9, 2, 1, 3))
print(solution(10, 18, 14, 18))