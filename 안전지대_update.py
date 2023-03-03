from pprint import pprint
import copy

def solution(board):
    answer = 0
    
    answer = len(board) * len(board[0])
    
    location = copy.deepcopy(board)
    
    for rows in range(len(board)):
        for cols in range(len(board[rows])):
            # print("[row,cols] is : [{0}, {1}]".format(rows, cols))
            # 지뢰 주변지역 location 위험지역(1)으로 변경
            if board[rows][cols] == 1: 
                
                # 첫째줄           
                if rows == 0:
                    if cols == 0: # (0,0) 위치
                        if rows+1 < len(board) and cols+1 < len(board[rows]):
                            location[rows][cols+1] = 1
                            location[rows+1][cols] = 1
                            location[rows+1][cols+1] = 1
                    elif 0 < cols < len(board[rows])-1: 
                        if rows+1 < len(board) and cols+1 < len(board[rows]):
                            location[rows][cols-1] = 1
                            location[rows][cols+1] = 1
                            location[rows+1][cols-1] = 1
                            location[rows+1][cols] = 1
                            location[rows+1][cols+1] = 1
                    else: # (0, 끝) 위치
                        if rows+1 < len(board):
                            location[rows][cols-1] = 1
                            location[rows+1][cols-1] = 1
                            location[rows+1][cols] = 1
                
                # 마지막줄    
                elif rows == len(board) -1: # (끝,0) 위치
                    if cols == 0:
                        if cols+1 < len(board[rows]):
                            location[rows-1][cols] = 1
                            location[rows-1][cols+1] = 1
                            location[rows][cols+1] = 1
                    elif 0 < cols < len(board[rows])-1:
                        if cols+1 < len(board[rows]):
                            location[rows][cols-1] = 1
                            location[rows][cols+1] = 1
                            location[rows-1][cols-1] = 1
                            location[rows-1][cols] = 1
                            location[rows-1][cols+1] = 1
                    else: # (끝,끝) 위치
                        location[rows][cols-1] = 1
                        location[rows-1][cols-1] = 1
                        location[rows-1][cols] = 1
                
                # 사이 줄    
                else:
                    if cols == 0: #(rows, 0) 위치
                        if cols+1 < len(board[rows]):
                            location[rows-1][cols] = 1
                            location[rows-1][cols+1] = 1
                            location[rows][cols+1] = 1
                            location[rows+1][cols] = 1
                            location[rows+1][cols+1] = 1
                    elif 0 < cols < len(board[rows])-1:
                        if cols+1 < len(board[rows]):
                            location[rows-1][cols-1] = 1
                            location[rows-1][cols] = 1
                            location[rows-1][cols+1] = 1
                            location[rows+1][cols-1] = 1
                            location[rows+1][cols] = 1
                            location[rows+1][cols+1] = 1
                            location[rows][cols-1] = 1
                            location[rows][cols+1] = 1
                    else: # (rows, 끝) 위치
                            location[rows-1][cols-1] = 1
                            location[rows-1][cols] = 1
                            location[rows+1][cols-1] = 1
                            location[rows+1][cols] = 1
                            location[rows][cols-1] = 1
    
    # pprint(board)
    # print("")
    # pprint(location)
    # 안전지대(0)인 지역 Count (전체 - count)
    for i in range(len(location)):
        for j in range(len(location[i])):
            if location[i][j] == 1:
                answer -= 1
            
    return answer

# 1
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
# 2
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
# 3
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))
# 4
print(solution([[0]]))
5
print(solution([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1]]))

print(solution([[0, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0]]))

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
