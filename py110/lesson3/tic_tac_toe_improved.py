import random
import os

# Cool color string tricks to print color text to terminal
PLAYER_TOKEN = "\033[34mX\033[0m"
COMPUTER_TOKEN = "\033[31mO\033[0m"
DEFAULT_TOKEN = " "
PLAYER = "player"
COMPUTER = "computer"


def prompt(message: str) -> None:
    print(f"=> {message}")


def initialize_board() -> dict[int, str]:
    return {num: DEFAULT_TOKEN for num in range(1, 10)}


def display_board(board: dict[int, str]) -> None:
    print("     |     |")
    print(f"  {board[1]}  |  {board[2]}  |   {board[3]}")
    print("     |     |")
    print("--1--+--2--+--3--")
    print("     |     |")
    print(f"  {board[4]}  |  {board[5]}  |   {board[6]}")
    print("     |     |")
    print("--4--+--5--+--6--")
    print("     |     |")
    print(f"  {board[7]}  |  {board[8]}  |   {board[9]}")
    print("     |     |")
    print("  7     8     9  ")


def get_possible_positions(board: dict[int, str]) -> list[int]:
    return [
        position
        for position, marker in board.items()
        if marker == DEFAULT_TOKEN
    ]


def player_turn(board: dict[int, str]) -> None:
    possible_positions = get_possible_positions(board)
    while True:
        prompt(
            f"Where would you like to place your piece? (You are {PLAYER_TOKEN})"
        )
        prompt(f"Possible positions: {possible_positions}")

        try:
            input_position = int(input())
        except ValueError:
            input_position = None
        if input_position in possible_positions:
            break  # Valid position

        prompt("Sorry, please select a valid position")

    update_board(board, PLAYER_TOKEN, input_position)


def computer_turn(board: dict[int, str]) -> None:
    # First set bot to pick a random choice
    selected_move = None

    # If there is a chance to win, pick the winning move
    for possible_move in get_possible_positions(board):
        if is_winning_move(possible_move, board, COMPUTER_TOKEN):
            selected_move = possible_move

    # If there is a chance to block player from winning, pick that move
    if selected_move is None:
        for possible_move in get_possible_positions(board):
            if is_winning_move(possible_move, board, PLAYER_TOKEN):
                selected_move = possible_move
    # Pick 5 as its the best centralizing move
    if selected_move is None and 5 in get_possible_positions(board):
        selected_move = 5
    # If computer still has not picked a move, make a random move
    if selected_move is None:
        selected_move = random.choice(get_possible_positions(board))

    update_board(board, COMPUTER_TOKEN, selected_move)
    prompt(f"Computer chose position: {selected_move}")


def update_board(board: dict[int, str], token: str, position: int) -> None:
    board[position] = token


def get_game_state(board: dict[int, str]) -> str:
    if did_current_player_win(board, PLAYER_TOKEN):
        return PLAYER
    if did_current_player_win(board, COMPUTER_TOKEN):
        return COMPUTER
    if not get_possible_positions(board):
        return "tied"

    return "playing"


def did_current_player_win(board: dict[int, str], current_token: str) -> bool:
    win_conditions = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    )

    for win_condition in win_conditions:
        if (
            board[win_condition[0]] == current_token
            and board[win_condition[1]] == current_token
            and board[win_condition[2]] == current_token
        ):
            return True

    return False


def get_round_number() -> int:
    while True:
        try:
            round_number = int(input().strip())
            if round_number < 1:
                raise ValueError
            break
        except ValueError:
            prompt("Please enter a valid positive integer")
    return round_number


def do_point_and_return_winner(board: dict[int, str]) -> str:
    while True:
        computer_turn(board)
        display_board(board)

        if get_game_state(board) != "playing":
            return get_game_state(board)

        player_turn(board)

        if get_game_state(board) != "playing":
            return get_game_state(board)

        os.system("clear")


def display_score(player_score: int, computer_score: int) -> None:
    prompt(
        f"Current Score:   Player {player_score} | {computer_score} Computer"
    )


def display_point_winner(point_winner: str) -> None:
    if point_winner == "tied":
        prompt("The game is tied!")
    else:
        prompt(f"Congrats to the {point_winner} for winning the point!")


def keep_playing_something() -> bool:
    while True:
        play_again = input().lower().strip()
        if play_again in ["y", "n", "yes", "no"]:
            break
        prompt("Sorry, please enter y, yes, n, or no")

    if play_again in ["n", "no"]:
        return False
    return True


def get_first_turn() -> str:
    current_turn = random.choice([PLAYER, COMPUTER])
    prompt(f"Randomly deciding who will go first: {current_turn}")
    return current_turn


def is_winning_move(
    move: int, current_board: dict[int, str], token: str
) -> bool:
    future_board = current_board.copy()
    update_board(future_board, token, move)

    if did_current_player_win(future_board, token):
        return True
    return False


def play_match(game_board: dict[int, str], max_rounds: int) -> None:
    player_score = 0
    computer_score = 0
    # Use max to select whichever is higher between player and computer score
    while max(player_score, computer_score) < max_rounds:
        os.system("clear")
        point_winner = None
        game_board = initialize_board()

        current_turn = get_first_turn()
        # This is for if the player goes first, we display the board then do
        # their turn. Afterwards play continues normally with computer always
        # going before player. Check do_point_and_return_winner to see details
        if current_turn == PLAYER:
            display_board(game_board)
            player_turn(game_board)
            os.system("clear")

        # Regular turn
        point_winner = do_point_and_return_winner(game_board)

        # Increments score
        if point_winner == PLAYER:
            player_score += 1
        elif point_winner == COMPUTER:
            computer_score += 1

        os.system("clear")
        display_board(game_board)
        display_point_winner(point_winner)
        display_score(player_score, computer_score)

        prompt("Would you like to keep playing the match? (y/n)")
        if not keep_playing_something():
            break

    os.system("clear")
    display_board(game_board)

    if player_score == max_rounds:
        prompt("Congrats for winning the match!")
    elif computer_score == max_rounds:
        prompt("Oof computer won the match. Better luck next time!")


def main() -> None:
    # Initialize board and counters
    game_board = initialize_board()
    keep_playing = True

    while keep_playing:
        os.system("clear")

        prompt("Welcome to Tic-Tac-Toe!")
        prompt("How many rounds would you like to play to? Ex: 3")
        max_rounds = get_round_number()

        play_match(game_board, max_rounds)

        prompt("Match has ended")
        prompt("Would you like to play another match? (y/n)")
        keep_playing = keep_playing_something()

    prompt("See you later!")


if __name__ == "__main__":
    main()
