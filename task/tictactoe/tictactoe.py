# write your code here
from collections import Counter


def input_chords():
    a, b = map(int, input("Enter the coordinates").split())
    print(a, b)
    if a > 3 or b > 3:
        return input_chords()
    if a < 1 or b < 1:
        return input_chords()

    if a == 1 and b == 1:
        return 6
    elif a == 1 and b == 2:
        return 3
    elif a == 1 and b == 3:
        return 0
    elif a == 2 and b == 1:
        return 7
    elif a == 2 and b == 2:
        return 4
    elif a == 2 and b == 3:
        return 1
    elif a == 3 and b == 1:
        return 8
    elif a == 3 and b == 2:
        return 5
    elif a == 3 and b == 3:
        return 2


def print_table(mas):
    print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------
""".format(*mas))


def input_X(index, turn):
    if mas[index] == '_':
        if not turn:
            mas[index] = 'X'
        else:
            mas[index] = 'O'
        print_table(mas)
    else:
        print("This cell is occupied! Choose another one!")
        index = input_chords()
        input_X(index, turn)


def check_win(board):
    count = Counter(board)
    X_win = False
    O_win = False
    if abs(count["X"] - count['O']) >= 2:
        return "Impossible"
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            if board[each[0]] == 'X':
                X_win = True
            elif board[each[0]] == 'O':
                O_win = True
    if X_win & O_win == True:
        return "Impossible"
    if X_win:
        return "X wins"
    if O_win:
        return "O wins"
    if '_' not in board:
        return 'Draw'
    if '_' in board:
        return "Game not finished"

    return 'Impossible'


mas = ['_' for i in range(9)]
turn = 1
print_table(mas)
for i in range(9):
    turn = 1 if turn == 0 else 0
    index = input_chords()
    input_X(index,turn)
    status = check_win(mas)
    if status == "X wins" or status == "O wins" or status == "Draw":
        print(status)
        break

# print(check_win(mas))
