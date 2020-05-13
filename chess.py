import sys

board = [
    # 0      #1     #2     #3     #4     #5     #6      #7
    [-5,    -3,    -4,    -9, -1000,    -4,    -3,    -5],   # 0
    [-1,    -1,    -1,    -1,    -1,    -1,    -1,    -1],   # 1
    [0,     0,     0,     0,     0,     0,     0,      0],   # 2
    [0,     0,     0,     0,     0,     0,     0,      0],   # 3
    [0,     0,     0,     9,     0,     0,     0,      0],   # 4
    [0,     0,     0,     0,     0,     0,     0,      0],   # 5
    [1,     1,     1,     1,     1,     1,     1,      1],   # 6
    [5,     3,     4,     9,  1000,     4,     3,      5],   # 7
]


def white_pawn_moves(x, y):
    moves = []
    if y > 0 and board[y-1][x] == 0:
        moves.append((x, y-1))  # 1x Forward
    if y == 6 and board[y-1][x] == 0 and board[y-2][x] == 0:
        moves.append((x, y-2))  # 2x Forward
    if y > 0 and x > 0 and board[y-1][x-1] < 0:  # Diagonal Left
        moves.append((x-1, y-1))
    if y > 0 and x < 7 and board[y-1][x+1] < 0:  # Diagonal Right
        moves.append((x+1, y-1))
    return moves

def white_rook_moves(x, y):
    moves = []
    for i in [1, 2, 3, 4, 5, 6, 7]:  # Up
        if y-i >= 0 and board[y-i][x] == 0:
            moves.append((x, y-i))
        elif y-i >= 0 and board[y-i][x] < 0:
            moves.append((x, y-i))
            break
        elif y-i >= 0 and board[y-i][x] > 0:
            break
    for i in [1, 2, 3, 4, 5, 6, 7]:  # Down
        if y+i <= 7 and board[y+i][x] == 0:
            moves.append((x, y+i))
        elif y+i <= 7 and board[y+i][x] < 0:
            moves.append((x, y+i))
            break
        elif y+i <= 7 and board[y+i][x] > 0:
            break
    for i in [1, 2, 3, 4, 5, 6, 7]:  # Right
        if x+i <= 7 and board[y][x+i] == 0:
            moves.append((x+i, y))
        elif x+i <= 7 and board[y][x+i] < 0:
            moves.append((x+i, y))
            break
        elif x+i <= 7 and board[y][x+i] > 0:
            break
    for i in [1, 2, 3, 4, 5, 6, 7]:  # Left
        if x-i >= 0 and board[y][x-i] == 0:
            moves.append((x-i, y))
        if x-i >= 0 and board[y][x-i] < 0:
            moves.append((x-i, y))
            break
        if x-i >= 0 and board[y][x-i] > 0:
            break
    return moves



def white_horse_moves(x, y):
    moves = []
    if y > 1 and x < 7 and board[y-2][x+1] <= 0:  # Up Right
        moves.append((x+1, y-2))
    if y > 1 and x > 0 and board[y-2][x-1] <= 0:  # Up Left
        moves.append((x-1, y-2))
    if y < 6 and x < 7 and board[y+2][x+1] <= 0:  # Down Right
        moves.append((x+1, y+2))
    if y < 6 and x > 0 and board[y+2][x-1] <= 0:  # Down Left
        moves.append((x-1, y+2))
    if y > 0 and x < 6 and board[y-1][x+2] <= 0:  # Right Up
        moves.append((x+2, y-1))
    if y < 7 and x < 6 and board[y+1][x+2] <= 0:  # Right Down
        moves.append((x+2, y+1))
    if y > 0 and x > 1 and board[y-1][x-2] <= 0:  # Left Up
        moves.append((x-2, y-1))
    if y < 7 and x > 1 and board[y+1][x-2] <= 0:  # Left Down
        moves.append((x-2, y+1))
    return moves

def white_bishop_moves(x, y):
    moves = []
    for i in [1, 2, 3, 4, 5, 6, 7]: # Right Down Diagonal
        if y-i >= 0 and x+i < 8 and board[y-i][x+i] == 0:
            moves.append((x+i, y-i))
        if y-i >= 0 and x+i < 8 and board[y-i][x+i] < 0:
            moves.append((x+i, y-i))
            break
        if y-i >= 0 and x+i < 8 and board[y-i][x+i] > 0:
            break
    for i in [1, 2, 3, 4, 5, 6, 7]: # Right Up Diagonal
        if y+i < 8 and x+i < 8 and board[y+i][x+i] == 0:
            moves.append((x+i, y+i))
        if y+i < 8 and x+i < 8 and board[y+i][x+i] < 0:
            moves.append((x+i, y+i))
            break
        if y+i < 8 and x+i < 8 and board[y+i][x+i] > 0:
            break
    for i in [1, 2, 3, 4, 5, 6, 7]: # Left Down Diagonal
        if y-i >= 0 and x-i >= 0 and board[y-i][x-i] == 0:
            moves.append((x-i, y-i))
        if y-i >= 0 and x-i >= 0 and board[y-i][x-i] < 0:
            moves.append((x-i, y-i))
            break
        if y-i >= 0 and x-i >= 0 and board[y-i][x-i] > 0:
            break
    for i in [1, 2, 3, 4, 5, 6, 7]: # Left Up Diagonal
        if y+i < 8 and x-i >= 0 and board[y+i][x-i] == 0:
            moves.append((x-i, y+i))
        if y+i < 8 and x-i >= 0 and board[y+i][x-i] < 0:
            moves.append((x-i, y+i))
            break;
        if y+i < 8 and x-i >= 0 and board[y+i][x-i] > 0:
            break;
    return moves

def white_queen_moves(x, y):
    return white_rook_moves(x, y) + white_bishop_moves(x, y)

def white_king_moves(x, y):
    moves = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if y+i >= 0 and y+i <= 7 and x+j >= 0 and x+j<=7 and board[y+i][x+j] <= 0:
                moves.append((x+j, y+i))
    return moves


def generate_moves(x, y):
    if board[y][x] == 1:  # Pawn
        return white_pawn_moves(x, y)
    elif board[y][x] == 5:  # Rook
        return white_rook_moves(x, y)
    elif board[y][x] == 3:  # Horse
        return white_horse_moves(x, y)
    elif board[y][x] == 4:  # Bishop
        return white_bishop_moves(x, y)
    elif board[y][x] == 9: # Queen
        return white_queen_moves(x, y)
    elif board[y][x] == 1000: # King
        return white_king_moves(x, y)


def print_board(b):
    for row in b:
        for i in row:
            print("{:6d},".format(i), end="")
            print()


print(generate_moves(int(sys.argv[1]), int(sys.argv[2])))
