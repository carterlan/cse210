#Standard Tic tac toe game
#Author: Landon Carter

def main():
    board = create_board()
    player = assign_player('')

    while not (if_win(board) or tie(board)):
        show_board(board)
        players_turn(player, board)
        player = assign_player(player)
    show_board(board)
    print('Good game. Thanks for playing!')

    if if_win(board) == True:
        player = assign_player(player)
        print(f'{player} is the winner')
    else:
        print("It's a Tie!")
        
#Create board
def create_board():
    board = []
    for i in range(9):
        board.append(i+1)
    return board

#Show board
def show_board(board):
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')

#assign player
def assign_player(new_player):
    if new_player == '' or new_player == 'o':
        return 'x'
    elif new_player == 'x': 
        return 'o'

#players Turn
def players_turn(player, board):
        turn = int(input(f"{player}'s turn to choose a square(1-9): "))
        board[turn - 1] = player

#if_Win
def if_win(board):
    while not (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6]):
            return False
    return True

#Tie
def tie(board):
    for i in range(9):
        if board[i] != 'x' and board[i] != 'o': 
            return(False)
    return True

if __name__ == "__main__":
    main()