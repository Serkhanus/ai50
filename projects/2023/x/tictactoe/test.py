import copy

import tictactoe as ttt
import sys
import time


user = None
board = ttt.initial_state()
ai_turn = False
gamer1 = None
states ={}
count = 0
count_x = 0

def fill_states(board):
    """
    a
    """
    global count, count_x
    opd_board_str = board_tostr(board)
    count +=1
    if states.get(opd_board_str, 0) is not None:
        return
    else:
        count_x +=1
        states[opd_board_str] = 0
        actions_list = ttt.actions(board)
        for action in actions_list:
            new_board = ttt.result(board, action)
            str_board = board_tostr(new_board)
            if states.get(str_board, 100):
                states[str_board] = None
                # new_board = str_toboard(str_board)
                fill_states(new_board)
    return

def board_tostr(board):
    string = (f'{board[0][0] if board[0][0] is not None else "-" }'
              f'{board[0][1] if board[0][1] is not None else "-" }'
              f'{board[0][2] if board[0][2] is not None else "-" }'
              f'{board[1][0] if board[1][0] is not None else "-" }'
              f'{board[1][1] if board[1][1] is not None else "-" }'
              f'{board[1][2] if board[1][2] is not None else "-" }'
              f'{board[2][0] if board[2][0] is not None else "-" }'
              f'{board[2][1] if board[2][1] is not None else "-" }'
              f'{board[2][2] if board[2][2] is not None else "-" }')
    return string


def str_toboard(str):
    board=[[str[0] if str[0] != '-' else None, str[1] if str[1] != '-' else None, str[2] if str[2] != '-' else None],
           [str[3] if str[3] != '-' else None, str[4] if str[4] != '-' else None, str[5] if str[5] != '-' else None],
           [str[6] if str[6] != '-' else None, str[7] if str[7] != '-' else None, str[8] if str[8] != '-' else None]]
    return board

states[board_tostr(board)]=None
start = time.time()
next_time = start
fill_states(board)
print(f'------------- {0}  ', len(states.keys()) )
end = time.time()
print(end-next_time)
next_time = end
# print(states)
a = copy.deepcopy(states)
end = time.time()
print(end-next_time)
next_time = end
# print(a)
for item in a.keys():
    a[item] = None
end = time.time()
print(end-next_time)
next_time = end
# print(a)
end = time.time()
print(end-start)

print(count)
print(count_x)
print(sys.getsizeof(states))
print(sys.getsizeof(a))

# for i in range(3):
#     for j in range(3):
#
#
# while not ttt.terminal(board):
#     gamer1 = ttt.player(board)
#     print(gamer1)
#     next_move = ttt.minimax(board)
#     board = ttt.result(board, next_move)
#     win = ttt.winner(board)
#     if win == ttt.X or win == ttt.O:
#         print(win+ " won ghe game")


