import os
import random


def clear_screen():
    os.system("clear")


def prompt(message):
    print(f"=> {message}")


class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    SUITS = ("hearts", "diamonds", "clubs", "spades")
    RANKS = (
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    )

    def __init__(self):
        self.refresh()

    def refresh(self):
        self.cards = [
            Card(suit, rank) for suit in Deck.SUITS for rank in Deck.RANKS
        ]
        self.shuffle()

    def deal(self):
        if not self.cards:
            self.refresh()
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)


class Participant:
    def __init__(self):
        self.hand = []

    def clear_hand(self):
        self.hand.clear()

    def is_busted(self):
        return self.hand_value() > 21

    def hand_value(self):
        current_sum = 0
        ace_counter = 0
        for card in self.hand:
            if card.rank.isdigit():
                current_sum += int(card.rank)
            elif card.rank in ["Jack", "Queen", "King"]:
                current_sum += 10
            else:
                ace_counter += 1
                current_sum += 1

        for _ in range(ace_counter):
            if current_sum + 10 <= 21:
                current_sum += 10

        return current_sum


class Player(Participant):
    def __init__(self, starting_balance=5):
        super().__init__()
        self.balance = starting_balance


class Dealer(Participant):
    def __init__(self):
        super().__init__()


class TwentyOneGame:
    WIN_AMOUNT = 10
    LOSE_AMOUNT = 0

    def __init__(self):
        self._deck = Deck()
        self._player = Player()
        self._dealer = Dealer()

    def start(self):
        clear_screen()
        self._display_welcome_message()

        while True:
            self._play_round()

            if self._player.balance >= TwentyOneGame.WIN_AMOUNT:
                prompt("Congrats you are rich!\n")
                break
            if self._player.balance <= TwentyOneGame.LOSE_AMOUNT:
                prompt("Uh oh you ran out of money!\n")
                break

            keep_playing = self._prompt_keep_playing()
            if not keep_playing:
                break
            clear_screen()

        self._display_goodbye_message()

    def _play_round(self):
        self._refresh_hands()
        self._deal_cards()
        self._show_cards()
        self._player_turn()
        if not self._player.is_busted():
            self._dealer_turn()
        self._display_result()
        self._update_balance()
        self._display_balance()

    def _refresh_hands(self):
        self._player.clear_hand()
        self._dealer.clear_hand()

    def _deal_cards(self):
        for _ in range(2):
            self._deal_to(self._player.hand)
            self._deal_to(self._dealer.hand)

    def _show_cards(self, hidden=True):
        if hidden:
            prompt(f"Dealer has: {self._dealer.hand[0].rank} and unknown card")
        else:
            dealer_prompt = "Dealer has:"
            dealer_cards = " and ".join(
                card.rank for card in self._dealer.hand
            )
            prompt(f"{dealer_prompt} {dealer_cards}")
            prompt(f"  Hand value: {self._dealer.hand_value()}")

        print()

        player_prompt = "Player has:"
        player_cards = " and ".join(card.rank for card in self._player.hand)
        prompt(f"{player_prompt} {player_cards}")
        prompt(f"  Hand value: {self._player.hand_value()}")

    def _player_turn(self):
        while True:
            stay_or_hit = self._prompt_hit_or_stay()
            if stay_or_hit in ["stay", "s"]:
                return

            self._deal_to(self._player.hand)
            clear_screen()
            self._show_cards()

            if self._player.is_busted():
                return

    def _dealer_turn(self):
        while self._dealer.hand_value() < 17:
            self._deal_to(self._dealer.hand)

    def _deal_to(self, target_hand):
        target_hand.append(self._deck.deal())

    def _display_welcome_message(self):
        prompt("Welcome to Twenty One!")

    def _display_goodbye_message(self):
        prompt("Thanks for playing! Goodbye!")

    def _determine_winner(self):
        player = self._player
        dealer = self._dealer
        if player.is_busted():
            return ("dealer", "You've busted! Oh no!")
        if dealer.is_busted():
            return ("player", "Dealer has busted.")
        if player.hand_value() > dealer.hand_value():
            return ("player", "Your hand is closer to 21!")
        if player.hand_value() < dealer.hand_value():
            return ("dealer", "Dealer's hand is closer to 21.")

        return ("tie", "Both hands have the same value!")

    def _display_result(self):
        clear_screen()
        self._show_cards(hidden=False)
        print()

        winner, reason = self._determine_winner()
        prompt(reason)
        match winner:
            case "player":
                prompt("You win!")
            case "dealer":
                prompt("Dealer wins!")
            case _:
                prompt("It's a tie!")

    def _update_balance(self):
        winner = self._determine_winner()[0]
        if winner == "player":
            self._player.balance += 1
        elif winner == "dealer":
            self._player.balance -= 1

    def _display_balance(self):
        print()
        prompt(f"Current balance: {self._player.balance}")

    def _prompt_keep_playing(self):
        while True:
            print()
            question = "Would you like to keep playing? (y/n): "
            keep_playing = input(question).strip().lower()
            if keep_playing in ["y", "n", "yes", "no"]:
                break
            prompt("Please enter yes (y) or no (n)")
        return keep_playing == "y"

    def _prompt_hit_or_stay(self):
        while True:
            print()
            question = "Would you like to stay (s) or hit (h)?: "
            stay_or_hit = input(question).strip().lower()
            if stay_or_hit in ["stay", "hit", "s", "h"]:
                break
            prompt("Please enter stay (s) or hit (h).")
        return stay_or_hit


game = TwentyOneGame()
game.start()
