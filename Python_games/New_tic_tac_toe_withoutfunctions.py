import random


board = ['NIL', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
n = input('Player 1 Choose(X/O): ').upper()

if n == 'X':
    n, o = 'X', 'O'
else:
    n, o = 'O', 'X'

turn = random.randint(0, 1)
if turn == 0:
    print('Player 1 will choose first')
else:
    print('Player 2 will choose first')

play_game = input('Ready to play?(Y/N): ').upper()
if play_game == 'Y':
    game_on = True
else:
    game_on = False

# player 1 turn
while game_on:
    if turn == 0:
        m = ' '
        while m not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print(board[1], '|', board[2], '|', board[3])
            print(board[4], '|', board[5], '|', board[6])
            print(board[7], '|', board[8], '|', board[9])
            m = int(input('player 1 place marker (1-9):'))
            if board[m] == o or board[m] == n or m not in range(1, 10):
                continue
            board[m] = n
            if board[1] == n and board[2] == n and board[3] == n or \
                    board[4] == n and board[5] == n and board[6] == n or \
                    board[7] == n and board[8] == n and board[9] == n or \
                    board[1] == n and board[4] == n and board[7] == n or \
                    board[2] == n and board[5] == n and board[8] == n or \
                    board[3] == n and board[6] == n and board[9] == n or \
                    board[1] == n and board[5] == n and board[9] == n or \
                    board[3] == n and board[5] == n and board[7] == n:
                print(board[1], '|', board[2], '|', board[3])
                print(board[4], '|', board[5], '|', board[6])
                print(board[7], '|', board[8], '|', board[9])
                print('Player 1 won!')
                game_on = False
            else:
                if ' ' not in board:
                    print(board[1], '|', board[2], '|', board[3])
                    print(board[4], '|', board[5], '|', board[6])
                    print(board[7], '|', board[8], '|', board[9])
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 1

    # player 2 turn
    if turn == 1:
        m = ' '
        while m not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print(board[1], '|', board[2], '|', board[3])
            print(board[4], '|', board[5], '|', board[6])
            print(board[7], '|', board[8], '|', board[9])
            m = int(input('player 2 place marker (1-9): '))
            if board[m] == n or board[m] == o or m not in range(1, 10):
                continue
            board[m] = o

            if board[1] == o and board[2] == o and board[3] == o or \
                    board[4] == o and board[5] == o and board[6] == o or \
                    board[7] == o and board[8] == o and board[9] == o or \
                    board[1] == o and board[4] == o and board[7] == o or \
                    board[2] == o and board[5] == o and board[8] == o or \
                    board[3] == o and board[6] == o and board[9] == o or \
                    board[1] == o and board[5] == o and board[9] == o or \
                    board[3] == o and board[5] == o and board[7] == o:
                print(board[1], '|', board[2], '|', board[3])
                print(board[4], '|', board[5], '|', board[6])
                print(board[7], '|', board[8], '|', board[9])
                print('Player 2 won!')
                game_on = False
            else:
                if ' ' not in board:
                    print(board[1], '|', board[2], '|', board[3])
                    print(board[4], '|', board[5], '|', board[6])
                    print(board[7], '|', board[8], '|', board[9])
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 0



