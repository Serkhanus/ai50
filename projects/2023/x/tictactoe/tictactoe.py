"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None
WIN_POSITIONS = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

boards = {}

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x, o = 0, 0
    for row in board:
        x += row.count(X)
        o += row.count(O)
    if x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                possible_actions.append((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    if i > 2 or i < 0 or j > 2 or j < 0 or board[i][j] is not None:
        raise IndexError
    result_board = copy.deepcopy(board)
    result_board[i][j] = player(board)
    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board):
        score = utility(board)
        if score == 1:
            return X
        elif score == -1:
            return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if if_winner(board, X) or if_winner(board, O):
        return True
    for row in board:
        if None in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if if_winner(board, X):
        return 1
    elif if_winner(board, O):
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    global boards
    boards.clear()
    if terminal(board) is True:
        return None
    # v = calculate_scores(board)
    v = calculate_scores_abp(board)
    return v[0]


def if_winner(board, gamer):
    """
    check win conditions
    """
    for row in WIN_POSITIONS:
        win = 0
        for check in row:
            if board[check[0]][check[1]] == gamer:
                win += 1
        if win == 3:
            return True
    return False


def calculate_scores(board):
    """
    reccursive score calculation - pure Minimax
    """
    possible_actions = actions(board)
    if len(possible_actions) == 9:
        return [(0,0), 0]
    delta_v = []
    crit = 0
    if player(board) == X:
        crit = -1
    else:
        crit = 1
    for action in possible_actions:
        new_board = result(board, action)
        if terminal(new_board):
            a = [action, utility(new_board)]
            return a
        else:
            y = calculate_scores(new_board)
            delta_v.append(y)

    for test in (crit, 0, -crit):
        for z, x in enumerate(delta_v):
            if x[1] == test:
                return [x[0], x[1]]



def calculate_scores2(board):
    """
    reccursive score calculation - pure Minimax
    """
    global boards
    local_boards = boards
    possible_actions = actions(board)
    if len(possible_actions) == 9:
        return [(0,0), 0]
    delta_v = []
    crit = 0
    if player(board) == X:
        crit = -1
    else:
        crit = 1
    for action in possible_actions:
        new_board = result(board, action)
        if local_boards.get(board_tostr(new_board)) is None:

            if terminal(new_board):
                a = [action, utility(new_board)]
                local_boards[board_tostr(new_board)] = a[1]
                return a
            else:
                y = calculate_scores2(new_board)
                if y is not None:
                    delta_v.append(y)
                    local_boards[board_tostr(new_board)] = y[1]

    for test in (crit, 0, -crit):
        for z, x in enumerate(delta_v):
            if x[1] == test:
                return [x[0], x[1]]


def calculate_scores_abp(board):
    """
    reccursive score calculation - Alpha-Beta Pruning - 1
    """
    global boards
    local_boards = boards
    possible_actions = actions(board)
    if len(possible_actions) == 9:
        return [(0,0), 0]
    delta_v = []
    crit = 0
    if player(board) == X:
        crit = -1
    else:
        crit = 1
    minmax = -crit
    for action in possible_actions:
        new_board = result(board, action)
        if local_boards.get(board_tostr(new_board)) is None:

            if terminal(new_board):
                a = [action, utility(new_board)]
                return a
            else:
                y = calculate_scores_abp(new_board)
                if y is not None:
                    if (crit == -1 and y[1] > minmax) or (crit == 1 and y[1] < minmax):
                        continue
                    elif (crit == -1 and y[1] < minmax) or (crit == 1 and y[1] > minmax):
                        minmax = y[1]
                        delta_v.append(y)
                    else:
                        delta_v.append(y)
                    local_boards[board_tostr(new_board)] = y[1]

    for test in (crit, 0, -crit):
        for z, x in enumerate(delta_v):
            if x[1] == test:
                return [x[0], x[1]]


def calculate_scores_abp2(board):
    """
    reccursive score calculation - Alpha-Beta Pruning - 1
    """

    possible_actions = actions(board)
    if len(possible_actions) == 9:
        return [(0,0), 0]
    delta_v = []
    crit = 0
    if player(board) == X:
        crit = -1
    else:
        crit = 1
    minmax = -crit
    for action in possible_actions:
        new_board = result(board, action)
        if terminal(new_board):
            a = [action, utility(new_board)]
            return a
        else:
            y = calculate_scores_abp(new_board)
            if y[1] == crit:
                return y
            else:
                delta_v.append(y)

    for test in (0, -crit):
        for z, x in enumerate(delta_v):
            if x[1] == test:
                return [x[0], x[1]]


def board_tostr(board):
    return (f'{board[0][0] if board[0][0] is not None else "-" }'
              f'{board[0][1] if board[0][1] is not None else "-" }'
              f'{board[0][2] if board[0][2] is not None else "-" }'
              f'{board[1][0] if board[1][0] is not None else "-" }'
              f'{board[1][1] if board[1][1] is not None else "-" }'
              f'{board[1][2] if board[1][2] is not None else "-" }'
              f'{board[2][0] if board[2][0] is not None else "-" }'
              f'{board[2][1] if board[2][1] is not None else "-" }'
              f'{board[2][2] if board[2][2] is not None else "-" }')



def str_toboard(str):
    return [[str[0] if str[0] != '-' else None, str[1] if str[1] != '-' else None, str[2] if str[2] != '-' else None],
           [str[3] if str[3] != '-' else None, str[4] if str[4] != '-' else None, str[5] if str[5] != '-' else None],
           [str[6] if str[6] != '-' else None, str[7] if str[7] != '-' else None, str[8] if str[8] != '-' else None]]