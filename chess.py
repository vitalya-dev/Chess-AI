import sys
import math
import copy

WHITE =  1
BLACK = -1
NONE  =  0

BOARD = [
    # 0      #1     #2     #3     #4     #5     #6      #7
    [-5,    -3,    -4,    -9, -1000,    -4,    -3,    -5],   # 0
    [-1,    -1,    -1,    -1,    -1,    -1,    -1,    -1],   # 1
    [0,     0,     0,     0,     0,     0,     0,      0],   # 2
    [0,     0,     0,     0,     0,     0,     0,      0],   # 3
    [0,     0,     0,     0,     0,     0,     0,      0],   # 4
    [0,    0,     0,     0,     0,     0,     0,      0],   # 5
    [1,     1,     1,     1,     1,     1,     1,      1],   # 6
    [5,     3,     4,     9,  1000,     4,     3,      5],   # 7
]

def who(a):
    if a < 0:
        return BLACK
    if a > 0:
        return WHITE
    if a == 0:
        return NONE


def make_move(move):
    BOARD[move[3]][move[2]] = BOARD[move[1]][move[0]]
    BOARD[move[1]][move[0]] = 0


def all_moves(player):
    moves = []
    for y in range(0, len(BOARD)):
        for x in range(0, len(BOARD[y])) :
            if who(BOARD[y][x]) == player:
                moves += generate_moves(x, y)
    return moves


def pawn_moves(x, y, player):
    moves = []
    if y > 0 and BOARD[y-player][x] == NONE:
        moves.append((x, y, x, y-player))  # 1x Forward
    if y > 0 and x > 0 and who(BOARD[y-player][x-1]) == -player:  # Diagonal Left
        moves.append((x, y, x-1, y-player))
    if y > 0 and x < 7 and who(BOARD[y-player][x+1]) == -player:  # Diagonal Right
        moves.append((x, y, x+1, y-player))
    return moves

def white_pawn_moves(x, y):
    moves = pawn_moves(x, y, WHITE)
    if y == 6 and BOARD[y-1][x] == 0 and BOARD[y-2][x] == 0:
        moves.append((x, y, x, y-2))  # 2x Forward
    return moves

def black_pawn_moves(x, y):
    moves = pawn_moves(x, y, BLACK)
    if y == 1 and BOARD[y+1][x] == 0 and BOARD[y+2][x] == 0:
        moves.append((x, y, x, y+2))  # 2x Forward
    return moves

def rook_moves(x, y, player):
    moves = []
    for i in [1, 2, 3, 4, 5, 6, 7]:  # Up
        if y-i >= 0 and BOARD[y-i][x] == 0:
            moves.append((x, y, x, y-i))
        elif y-i >= 0 and who(BOARD[y-i][x]) == -player:
            moves.append((x, y, x, y-i))
            break
        elif y-i >= 0 and who(BOARD[y-i][x]) == player:
            break
    for i in [1, 2, 3, 4, 5, 6, 7]:  # Down
        if y+i <= 7 and BOARD[y+i][x] == 0:
            moves.append((x, y, x, y+i))
        elif y+i <= 7 and who(BOARD[y+i][x]) == -player:
            moves.append((x, y, x, y+i))
            break
        elif y+i <= 7 and who(BOARD[y+i][x]) == player:
            break
    for i in [1, 2, 3, 4, 5, 6, 7]:  # Right
        if x+i <= 7 and BOARD[y][x+i] == 0:
            moves.append((x, y, x+i, y))
        elif x+i <= 7 and who(BOARD[y][x+i]) == -player:
            moves.append((x, y, x+i, y))
            break
        elif x+i <= 7 and who(BOARD[y][x+i]) == player:
            break
    for i in [1, 2, 3, 4, 5, 6, 7]:  # Left
        if x-i >= 0 and BOARD[y][x-i] == 0:
            moves.append((x, y, x-i, y))
        elif x-i >= 0 and who(BOARD[y][x-i]) == -player:
            moves.append((x, y, x-i, y))
            break
        elif x-i >= 0 and who(BOARD[y][x-i]) == player:
            break
    return moves


def white_rook_moves(x, y):
    return rook_moves(x, y, WHITE)

def black_rook_moves(x, y):
    return rook_moves(x, y, BLACK)

def horse_moves(x, y, player):
    moves = []
    if y > 1 and x < 7 and (BOARD[y-2][x+1] == 0 or who(BOARD[y-2][x+1]) == -player):  # Up Right
        moves.append((x, y, x+1, y-2))
    if y > 1 and x > 0 and (BOARD[y-2][x-1] == 0 or who(BOARD[y-2][x-1]) == -player):  # Up Left
        moves.append((x, y, x-1, y-2))
    if y < 6 and x < 7 and (BOARD[y+2][x+1] == 0 or who(BOARD[y+2][x+1]) == -player):  # Down Right
        moves.append((x, y, x+1, y+2))
    if y < 6 and x > 0 and (BOARD[y+2][x-1] == 0 or who(BOARD[y+2][x-1]) == -player):  # Down Left
        moves.append((x, y, x-1, y+2))
    if y > 0 and x < 6 and (BOARD[y-1][x+2] == 0 or who(BOARD[y-1][x+2]) == -player):  # Right Up
        moves.append((x, y, x+2, y-1))
    if y < 7 and x < 6 and (BOARD[y+1][x+2] == 0 or who(BOARD[y+1][x+2]) == -player):  # Right Down
        moves.append((x, y, x+2, y+1))
    if y > 0 and x > 1 and (BOARD[y-1][x-2] == 0 or who(BOARD[y-1][x-2]) == -player):  # Left Up
        moves.append((x, y, x-2, y-1))
    if y < 7 and x > 1 and (BOARD[y+1][x-2] == 0 or who(BOARD[y+1][x-2]) == -player):  # Left Down
        moves.append((x, y, x-2, y+1))
    return moves

def white_horse_moves(x, y):
    return horse_moves(x, y, WHITE)

def black_horse_moves(x, y):
    return horse_moves(x, y, BLACK)


def bishop_moves(x, y, player):
    moves = []
    for i in [1, 2, 3, 4, 5, 6, 7]: # Right Down Diagonal
        if y-i >= 0 and x+i < 8 and BOARD[y-i][x+i] == 0:
            moves.append((x, y, x+i, y-i))
        elif y-i >= 0 and x+i < 8 and who(BOARD[y-i][x+i]) == -player:
            moves.append((x, y, x+i, y-i))
            break
        elif y-i >= 0 and x+i < 8 and who(BOARD[y-i][x+i]) == player:
            break
    for i in [1, 2, 3, 4, 5, 6, 7]: # Right Up Diagonal
        if y+i < 8 and x+i < 8 and BOARD[y+i][x+i] == 0:
            moves.append((x, y, x+i, y+i))
        elif y+i < 8 and x+i < 8 and who(BOARD[y+i][x+i]) == -player:
            moves.append((x, y, x+i, y+i))
            break
        elif y+i < 8 and x+i < 8 and who(BOARD[y+i][x+i]) == player:
            break
    for i in [1, 2, 3, 4, 5, 6, 7]: # Left Down Diagonal
        if y-i >= 0 and x-i >= 0 and BOARD[y-i][x-i] == 0:
            moves.append((x, y, x-i, y-i))
        elif y-i >= 0 and x-i >= 0 and who(BOARD[y-i][x-i]) == -player:
            moves.append((x, y, x-i, y-i))
            break
        elif y-i >= 0 and x-i >= 0 and who(BOARD[y-i][x-i]) == player:
            break
    for i in [1, 2, 3, 4, 5, 6, 7]: # Left Up Diagonal
        if y+i < 8 and x-i >= 0 and BOARD[y+i][x-i] == 0:
            moves.append((x, y, x-i, y+i))
        elif y+i < 8 and x-i >= 0 and who(BOARD[y+i][x-i]) == -player:
            moves.append((x, y, x-i, y+i))
            break;
        elif y+i < 8 and x-i >= 0 and who(BOARD[y+i][x-i]) == player:
            break;
    return moves

def white_bishop_moves(x, y):
    return bishop_moves(x, y, WHITE)

def black_bishop_moves(x, y):
    return bishop_moves(x, y, BLACK)

def white_queen_moves(x, y):
    return rook_moves(x, y, WHITE) + bishop_moves(x, y, WHITE)

def black_queen_moves(x, y):
    return rook_moves(x, y, BLACK) + bishop_moves(x, y, BLACK)


def king_moves(x, y, player):
    moves = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if y+i < 0 or y+i > 7 or x+j < 0 or x+j > 7:
                continue
            elif BOARD[y+i][x+j] == 0 or who(BOARD[y+i][x+j]) == -player:
                moves.append((x, y, x+j, y+i))
    return moves

def white_king_moves(x, y):
    return king_moves(x, y, WHITE)

def black_king_moves(x, y):
    return king_moves(x, y, BLACK)


def generate_moves(x, y):
    if BOARD[y][x] == 1:  # White Pawn
        return white_pawn_moves(x, y)
    if BOARD[y][x] == -1:  # Black Pawn
        return black_pawn_moves(x, y)
    elif BOARD[y][x] == 5:  # White Rook
        return white_rook_moves(x, y)
    elif BOARD[y][x] == -5:  # Black Rook
        return black_rook_moves(x, y)
    elif BOARD[y][x] == 3:  # White Horse
        return white_horse_moves(x, y)
    elif BOARD[y][x] == -3:  # Black Horse
        return black_horse_moves(x, y)
    elif BOARD[y][x] == 4:  #  White Bishop
        return white_bishop_moves(x, y)
    elif BOARD[y][x] == -4:  # Black Bishop
        return black_bishop_moves(x, y)
    elif BOARD[y][x] == 9: #  White Queen
        return white_queen_moves(x, y)
    elif BOARD[y][x] == -9: #  Black Queen
        return black_queen_moves(x, y)
    elif BOARD[y][x] == 1000: # White King
        return white_king_moves(x, y)
    elif BOARD[y][x] == -1000: # Black King
        return black_king_moves(x, y)


def print_board():
    for row in BOARD:
        for i in row:
            print("{:6d},".format(i), end="")
        print()

def score():
    return sum([sum(row) for row in BOARD])

def best_move(player):
    global BOARD
    #####################################
    bm = None
    for move in all_moves(player):
        board = copy.deepcopy(BOARD)
        #####################################
        make_move(move)
        if bm == None:
            bm = [move, score()]
        if player == BLACK and score() < bm[1]:
            bm = [move, score()]
        if player == WHITE and score() > bm[1]:
            bm = [move, score()]
        #####################################
        BOARD = board
    return bm

if __name__ == '__main__':
    print(best_move(WHITE))
