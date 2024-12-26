import random
import os

os.system("clear")


class Player:
    CHOICES = ("rock", "paper", "scissors")

    def __init__(self) -> None:
        self.move = None
        self.score = 0


class Computer(Player):
    def __init__(self) -> None:
        super().__init__()

    def choose(self) -> None:
        self.move = random.choice(Player.CHOICES)


class Human(Player):
    def __init__(self) -> None:
        super().__init__()

    def choose(self) -> None:
        prompt = "Please choose rock, paper, scissors, lizard, or spock: "

        while True:
            choice = input(prompt).lower()
            if choice.lower() in Player.CHOICES:
                break

            print(f"Sorry, {choice} is not valid")

        self.move = choice


# See if you can figure out a way to add a Move class with 5 additional classes (Rock, Paper, Scissors, Lizard, and Spock) that handle each kind of move. How would the code change? Can you make it work? After you're done, can you talk about whether this was a good design decision? What are the pros/cons?
class Move:
    def wins_against(self, other) -> bool:
        return str(other) in self.wins

    def loses_against(self, other) -> bool:
        return str(other) in self.loses


class Rock(Move):
    def __init__(self) -> None:
        self.wins = ("scissors", "lizard")
        self.loses = ("paper", "spock")

    def __str__(self) -> str:
        return "rock"


class Paper(Move):
    def __init__(self) -> None:
        self.wins = ("rock", "spock")
        self.loses = ("scissors", "lizard")

    def __str__(self) -> str:
        return "paper"


class Scissors(Move):
    def __init__(self) -> None:
        self.wins = ("paper", "lizard")
        self.loses = ("rock", "spock")

    def __str__(self) -> str:
        return "scissors"


class Lizard(Move):
    def __init__(self) -> None:
        self.wins = ("spock", "paper")
        self.loses = ("rock", "scissors")

    def __str__(self) -> str:
        return "lizard"


class Spock(Move):
    def __init__(self) -> None:
        self.wins = ("rock", "scissors")
        self.loses = ("lizard", "paper")

    def __str__(self) -> str:
        return "spock"


class RPSGame:
    def __init__(self) -> None:
        self._human = Human()
        self._computer = Computer()

    @staticmethod
    def _display_welcome_message() -> None:
        print("Welcome to Rock Paper Scissors!")

    @staticmethod
    def _display_goodbye_message() -> None:
        print("Thanks for playing Rock Paper Scissors. Goodbye!")

    def _human_wins(self) -> bool:
        human_move = self._human.move
        computer_move = self._computer.move

        return (
            (human_move == "rock" and computer_move == "scissors")
            or (human_move == "paper" and computer_move == "rock")
            or (human_move == "scissors" and computer_move == "paper")
        )

    def _computer_wins(self) -> bool:
        human_move = self._human.move
        computer_move = self._computer.move

        return (
            (computer_move == "rock" and human_move == "scissors")
            or (computer_move == "paper" and human_move == "rock")
            or (computer_move == "scissors" and human_move == "paper")
        )

    def _display_winner(self) -> None:
        print(f"You chose: {self._human.move}")
        print(f"The computer chose: {self._computer.move}")

        if self._human_wins():
            print("You win!")
        elif self._computer_wins():
            print("Computer wins!")
        else:
            print("It's a tie")

    def _calculate_score(self) -> None:
        if self._human_wins():
            self._human.score += 1
        elif self._computer_wins():
            self._computer.score += 1

    def _display_score(self) -> None:
        print(
            f"Score:  Player {self._human.score} | Computer {self._computer.score}"
        )

    def play(self) -> None:
        self._display_welcome_message()

        while True:
            os.system("clear")
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            self._calculate_score()
            self._display_score()
            if not self._play_again():
                break

        self._display_goodbye_message()

    def _play_again(self) -> bool:
        answer = input("Would you like to play again? (y/n) ")
        return answer.lower().startswith("y")


RPSGame().play()
