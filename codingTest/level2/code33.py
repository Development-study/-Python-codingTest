# 혼자서 하는 틱택토 (프로그래머스 2단계 문제)

from collections import Counter

def solution(board):
    o_count, x_count, o_win, x_win = 0, 0, 0, 0
    
    for tic in board:
        o_count += Counter(tic)['O']
        x_count += Counter(tic)['X']
    
        
    if o_count + x_count == 0:
        return 1
    elif x_count > o_count:
        return 0
    elif x_count + 1 < o_count:
        return 0
    
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == "O":
                o_win += 1
            elif board[0][i] == "X":
                x_win += 1
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == "O":
                o_win += 1
            elif board[i][0] == "X":
                x_win += 1
    
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == "O":
            o_win += 1
        elif board[0][0] == "X":
            x_win += 1
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == "O":
            o_win += 1
        elif board[0][2] == "X":
            x_win += 1
    
    if o_win == x_win and o_win == 0:
        return 1
    elif x_win == 0 and o_win > 0:
        if x_count < o_count:
            return 1
    elif x_win > 0 and o_win == 0:
        if x_count == o_count:
            return 1
    
    return 0

board = ["O.X", ".O.", "..X"]
print(solution(board))