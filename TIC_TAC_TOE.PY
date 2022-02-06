import random
import os
def clear_output(): return os.system('cls')


def display_board(board):
    clear_output()
    print(' '+' | '+' '+' | '+' ')
    print(board[7]+' | '+board[8]+' | '+board[9])
    print(' '+' | '+' '+' | '+' ')
    print('-'*9)
    print(' '+' | '+' '+' | '+' ')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print(' '+' | '+' '+' | '+' ')
    print('-'*9)
    print(' '+' | '+' '+' | '+' ')
    print(board[1]+' | '+board[2]+' | '+board[3])
    print(' '+' | '+' '+' | '+' ')


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = (input('Player 1: Do you want to be X or O? ').upper())

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)


def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, mark):
    for n in board:
        return (board[7] == board[8] == board[9] == mark or
                board[4] == board[5] == board[6] == mark or
                board[1] == board[2] == board[3] == mark or
                board[1] == board[4] == board[7] == mark or
                board[2] == board[5] == board[8] == mark or
                board[3] == board[6] == board[9] == mark or
                board[1] == board[5] == board[9] == mark or
                board[3] == board[5] == board[7] == mark)


def choose_first():
    if random.randint(0, 1) == 0:
        return('Player1 will go first', 0)
    else:
        return('Player2 will go first', 1)


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for n in board:
        if n == 'X' or n == 'O':
            pass
        else:
            return False
    return True


def player_choice(board):
    while True:
        position = 0
        while position not in range(1, len(board)):
            try:
                position = int(input('Enter your next position (1-9): '))
            except:
                print("That's not a valid option!")
        if space_check(board, position):
            return position
        else:
            pass


def replay():
    replay_game = 'Y'
    while replay_game != 'Y' or replay_game != 'N':
        replay_game = (input('Do you want to play again? (Y/N) :').upper())
        if replay_game == 'Y':
            return True
        elif replay_game == 'N':
            return False
        else:
            pass


def startgame():
    start_game = 'Y'
    while start_game != 'Y' or start_game != 'N':
        start_game = (input('Are you ready to play the game? (Y/N) :').upper())
        if start_game == 'Y':
            return True
        elif start_game == 'N':
            return False
        else:
            pass


print('Welcome to Tic Tac Toe!')
player1_marker, player2_marker = player_input()
text, player_flag = choose_first()
print(text)
while startgame():
    game_on = True
    board = ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(board)
    while game_on:
        while player_flag == 0:
            position = player_choice(board)
            marker = player1_marker
            place_marker(board, marker, position)
            display_board(board)
            if win_check(board, marker):
                print('Player 1 won!')
                game_on = False
                break
            if full_board_check(board):
                print('Draw')
                game_on = False
                break
            player_flag = 1

        while player_flag == 1:
            position = player_choice(board)
            marker = player2_marker
            place_marker(board, marker, position)
            display_board(board)
            if win_check(board, marker):
                print('Player 2 won!')
                game_on = False
                break
            if full_board_check(board):
                print('Draw')
                game_on = False
                break
            player_flag = 0

    if not replay():
        break
