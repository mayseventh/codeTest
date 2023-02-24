def solution(keyinput, board):
    answer = [0, 0]

    for i in keyinput:
        print("direction is : {0}".format(i))
        if i == "left":
            answer[0] -= 1
            if abs(answer[0]) > abs(board[0]//2):
                answer[0] += 1
        elif i == "right":
            answer[0] += 1
            if abs(answer[0]) > abs(board[0]//2):
                answer[0] -= 1
        elif i == "up":
            answer[1] += 1
            if abs(answer[1]) > abs(board[1]//2):
                answer[1] -= 1
        elif i == "down":
            answer[1] -= 1
            if abs(answer[1]) > abs(board[1]//2):
                answer[1] += 1
        print(answer)
        
    return answer

# print(solution(["left", "right", "up", "right", "right"], [11, 11]))
# print(solution(["down", "down", "down", "down", "down"], [7, 9]))
print(solution(["left", "left", "left", "left", "right", "right", "right", "right"], [5,5]))