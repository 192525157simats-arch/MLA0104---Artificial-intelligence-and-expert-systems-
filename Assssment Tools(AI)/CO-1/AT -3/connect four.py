import math

ROWS = 6
COLS = 7

board = [[" "]*COLS for _ in range(ROWS)]

def print_board():
    for row in board:
        print("|".join(row))
    print("-"*15)

def drop(col, piece):
    for r in range(ROWS-1,-1,-1):
        if board[r][col] == " ":
            board[r][col] = piece
            return True
    return False

def available():
    return [c for c in range(COLS) if board[0][c]==" "]

def minimax(depth, maximizing):
    if depth == 0:
        return 0

    if maximizing:
        value = -math.inf
        for col in available():
            drop(col,"X")
            value = max(value,minimax(depth-1,False))
            for r in range(ROWS):
                if board[r][col]=="X":
                    board[r][col]=" "
                    break
        return value
    else:
        value = math.inf
        for col in available():
            drop(col,"O")
            value = min(value,minimax(depth-1,True))
            for r in range(ROWS):
                if board[r][col]=="O":
                    board[r][col]=" "
                    break
        return value

print("Simple Connect Four AI Example")
print_board()
