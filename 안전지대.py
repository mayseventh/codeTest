from pprint import pprint

def solution(board):
    answer = 0
    check = []

    print(len(board))
    print(len(board[0]))

    for i in range(len(board)):
        if len(board) == 1 and board[0] == 1:
            answer = 0
            break
        elif len(board) == 1 and board[0] == 0:
            answer = 1
            break
    
        for j in range(len(board[i])):
            if board[i][j] == 1:
                check.append(1)
    
            if i == 0:
                if j == 0:
                    check.append(board[i][j+1])
                    check.append(board[i+1][j])
                    check.append(board[i+1][j+1])
                elif j == len(board[i])-1:
                    check.append(board[i][j-1])
                    check.append(board[i+1][j-1])
                    check.append(board[i+1][j])
                else:
                    check.append(board[i][j-1])
                    check.append(board[i][j+1])
                    check.append(board[i+1][j-1])
                    check.append(board[i+1][j])
                    check.append(board[i+1][j+1])

            elif i == len(board)-1:
                if j == 0:
                    check.append(board[i-1][j])
                    check.append(board[i-1][j+1])
                    check.append(board[i][j+1])
                elif j == len(board[i])-1:
                    check.append(board[i][j-1])
                    check.append(board[i-1][j-1])
                    check.append(board[i-1][j])
                else:
                    check.append(board[i][j-1])
                    check.append(board[i][j+1])
                    check.append(board[i-1][j-1])
                    check.append(board[i-1][j])
                    check.append(board[i-1][j+1])

            else:
                if j == 0:
                    check.append(board[i-1][j])
                    check.append(board[i+1][j])
                    check.append(board[i-1][j+1])
                    check.append(board[i][j+1])
                    check.append(board[i+1][j+1])
                elif j == len(board[i])-1:
                    check.append(board[i-1][j])
                    check.append(board[i+1][j])
                    check.append(board[i-1][j-1])
                    check.append(board[i][j-1])
                    check.append(board[i+1][j-1])
                else:
                    check.append(board[i-1][j-1])
                    check.append(board[i-1][j])
                    check.append(board[i-1][j+1])
                    check.append(board[i][j-1])
                    check.append(board[i][j+1])
                    check.append(board[i+1][j-1])
                    check.append(board[i+1][j])
                    check.append(board[i+1][j+1])

            pprint(check)
            if check.count(1) == 0:
                answer += 1
            
            print("************  i, j, count is : {0}, {1}, {2}".format(i, j, check.count(1)))
            check = []

    return answer

#1
# print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
#2
# print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
# #3
# print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))
# 4
print(solution([[0]]))
