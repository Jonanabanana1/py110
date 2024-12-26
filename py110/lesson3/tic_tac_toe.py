# 1) Display the initial empty 3x3 board.
# 2) Ask the user to mark a square.
# 3) Computer marks a square.
# 4) Display the updated board state.
# 5) If it's a winning board, display the winner.
# 6) If the board is full, display tie.
# 7) If neither player won and the board is not full, go to #2
# 8) Play again?
# 9) If yes, go to #1
# 10) Goodbye!

# 1) Display the initial empty 3x3 board
# Input:
#   - String User = Player or Computer
#   - List coordinates (0, 2)
# Output:
#   - Print Board with updated state
# Data Structures:
#   - Dictionary: keys=coordinate, value=state(either ' ', 'X', or 'O')
import random

ROWS = 3
COLUMNS = 3
PLAYER = "player"
COMPUTER = "computer"
PLAYER_PIECE = "X"
COMPUTER_PIECE = "O"


def update_board(user: str, position: tuple[int, int], board) -> None:
    piece = PLAYER_PIECE if user == "player" else COMPUTER_PIECE
    board[position] = piece


def initialize_board():
    return {(row, column): " " for row in range(ROWS) for column in range(COLUMNS)}


def display_board(board) -> None:
    print("     |     |     ")
    print(f"  {board[(0, 0)]}  |  {board[(0, 1)]}  |  {board[(0, 2)]}")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {board[(1, 0)]}  |  {board[(1, 1)]}  |  {board[(1, 2)]}")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {board[(2, 0)]}  |  {board[(2, 1)]}  |  {board[(2, 2)]}")
    print("     |     |     ")


def player_input_string_to_tuple(input_string: str):
    cleaned_input = [char for char in input_string if char.isdigit()]
    if len(cleaned_input) < 2:
        return None
    x_coordinate = int(cleaned_input[0])
    y_coordinate = int(cleaned_input[1])
    return (x_coordinate, y_coordinate)


def get_possible_positions(board):
    return [position for position in board if board[position] == " "]


def do_player_turn(board) -> None:
    while True:
        print("Where would you like to place your piece?")
        print(f"Possible positions:\n{get_possible_positions(board)}")
        selected_position = player_input_string_to_tuple(input())
        if selected_position in get_possible_positions(board):
            break
        print("Sorry, please choose a valid position")
    update_board(user="player", position=selected_position, board=board)
    display_board(board)
    # print(selected_position)


def do_computer_turn(board) -> None:

    selected_position = random.choice(get_possible_positions(board))
    update_board(user="computer", position=selected_position, board=board)
    print(f"Computer chose position: {selected_position}")
    display_board(board)
    # print(selected_position)


def is_winning_board(user: str, board):
    piece = PLAYER_PIECE if user == "player" else COMPUTER_PIECE
    top_row = [board[(0, 0)], board[0, 1], board[0, 2]]
    middle_row = [board[(1, 0)], board[1, 1], board[1, 2]]
    bottom_row = [board[(2, 0)], board[2, 1], board[2, 2]]
    first_column = [board[0, 0], board[1, 0], board[2, 0]]
    second_column = [board[0, 1], board[1, 1], board[2, 1]]
    third_column = [board[0, 2], board[1, 2], board[2, 2]]
    left_diagonal = [board[0, 0], board[1, 1], board[2, 2]]
    right_diagonal = [board[2, 0], board[1, 1], board[0, 2]]

    win_conditions = [
        top_row,
        middle_row,
        bottom_row,
        first_column,
        second_column,
        third_column,
        left_diagonal,
        right_diagonal,
    ]
    win_counter = 0
    for win_condition in win_conditions:
        for board_pieces in win_condition:
            for board_piece in board_pieces:
                if piece == board_piece:
                    win_counter += 1
                if win_counter == 3:
                    return True
        win_counter = 0
    return False


def is_tied_board(board):
    return get_possible_positions(board) == []


def main():
    while True:
        print("Welcome to tic-tac-toe!")
        print("Deciding who will go first...")
        board = initialize_board()
        if random.randint(0, 1) == 0:
            print("You will go first!")
            first_turn = PLAYER
        else:
            print("Computer will go first!")
            first_turn = COMPUTER

        while True:
            if first_turn == PLAYER:
                do_player_turn(board)
                if is_winning_board(PLAYER, board) or is_tied_board(board):
                    break
                do_computer_turn(board)
                if is_winning_board(COMPUTER, board) or is_tied_board(board):
                    break
            else:
                do_computer_turn(board)
                if is_winning_board(PLAYER, board) or is_tied_board(board):
                    break
                do_player_turn(board)
                if is_winning_board(COMPUTER, board) or is_tied_board(board):
                    break
        if is_tied_board(board):
            print("Itsa tie!")
        elif is_winning_board(PLAYER, board):
            print("Congrats for winning!")
        else:
            print("Wuh woh try again :/")

        board = {(row, column): " " for row in range(ROWS) for column in range(COLUMNS)}
        print("Would you like to player again? (y/n)")
        play_again = input()
        if play_again == "n":
            break


if __name__ == "__main__":
    main()
