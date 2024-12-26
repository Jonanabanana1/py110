from os import system

system("clear")
# Your task is to write a CircularBuffer class in Python that implements a circular buffer for arbitrary objects. The class should be initialized with the buffer size and provide the following methods:

# put: Add an object to the buffer
# get: Remove (and return) the oldest object in the buffer. Return None if the buffer is empty.

# You may assume that none of the values stored in the buffer are None (however, None may be used to designate empty spots in the buffer).
"""
Data Strucuture:
    List to contain elements in buffer
    List size is equal to buffer size in input
    Initialize list to contain None 

    order list that is same size as previous list but this one will contain numbers representing the insertion order
Put:
    Check from ending position in list to start position for None values.
    If a none is found, replace the None with the input element. If no elements are none, invoke get() and try again
    When you add an element, increment a element counter variable and add the variable to the order list at the same index.
Get:
    Iterate through order list, and determine which index has the lowest value. The index with the lowest value, replace and capture the same index element from the buffer list with None. 

"""


class CircularBuffer:
    def __init__(self, size) -> None:
        self._order_list = []
        self._buffer_list = [None] * size
        self._next_insert_idx = 0

    def put(self, obj):
        self._buffer_list[self._next_insert_idx] = obj
        self._order_list.append(self._next_insert_idx)
        self._next_insert_idx += 1
        if self._next_insert_idx == len(self._buffer_list):
            self._next_insert_idx = 0
        if len(self._order_list) > len(self._buffer_list):
            self._order_list.pop(0)

    def get(self):
        if self._order_list == []:
            return None
        remove_idx = self._order_list.pop(0)
        remove_value = self._buffer_list[remove_idx]
        self._buffer_list[remove_idx] = None
        return remove_value


# Create an object-oriented number guessing class for numbers in the range 1 to 100, with a limit of 7 guesses per game. The game should play like this:
import random
import math


class GuessingGame:
    def __init__(self, lower_limit=1, upper_limit=100) -> None:
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit
        self.guesses_amount = int(math.log2(upper_limit - lower_limit + 1)) + 1
        self.reset_game()

    def play(self):
        while self.guesses_amount >= 1:
            print(f"You have {self.guesses_amount} guesses remaining")
            user_guess = self._check_valid_guess()
            print(self._guess_proximity(user_guess))
            if user_guess == self.correct_guess:
                print("\nYou won!")
                break
            self.guesses_amount -= 1
        if self.guesses_amount == 0:
            print("\nYou have no more guesses. You lost!")
        self.reset_game()

    def reset_game(self):
        self.guesses_amount = (
            int(math.log2(self.upper_limit - self.lower_limit + 1)) + 1
        )
        self.correct_guess = random.randint(self.lower_limit, self.upper_limit)

    def _guess_proximity(self, guess):
        if guess < self.correct_guess:
            return "Your guess is too low."
        if guess > self.correct_guess:
            return "Your guess is too high."
        return "That's the number!"

    def _check_valid_guess(self):
        while True:
            try:
                user_guess = int(
                    input(
                        f"Enter a number between {self.lower_limit} and {self.upper_limit}: "
                    )
                )
                if self.lower_limit <= user_guess <= self.upper_limit:
                    return user_guess
                raise ValueError
            except ValueError:
                print("Invalid guess. ", end="")


# game = GuessingGame(500, 1500)
# game.play()


# Update this class so you can use it to determine the lowest ranking and highest ranking cards in a list of Card objects:
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.value < other.value

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def value(self):
        match self.rank:
            case "Jack":
                return 11
            case "Queen":
                return 12
            case "King":
                return 13
            case "Ace":
                return 14
            case _:
                return int(self.rank)


# If you have two or more cards of the same rank in your list, your min and max methods should return one of the matching cards; it doesn't matter which one.

# Besides any methods needed to determine the lowest and highest cards, create a __str__ method that returns a string representation of the card, e.g., "Jack of Diamonds", "4 of Clubs", etc.


# Using the Card class from the previous exercise, create a Deck class that contains all of the standard 52 playing cards. Use the following code to start your work:
# The Deck class should provide a draw method to deal one card. The Deck should be shuffled when it is initialized. If no more cards remain when draw is called, the method should generate a new set of 52 shuffled cards, then deal one card from the new cards.
class Deck:
    RANKS = list(range(2, 11)) + ["Jack", "Queen", "King", "Ace"]
    SUITS = ["Hearts", "Clubs", "Diamonds", "Spades"]

    def __init__(self) -> None:
        self.cards = self.generate_shuffled_cards()

    def generate_shuffled_cards(self):
        cards = [
            Card(rank, suit)
            for suit in self.__class__.SUITS
            for rank in self.__class__.RANKS
        ]
        random.shuffle(cards)
        return cards

    def draw(self):
        if not self.cards:
            self.cards = self.generate_shuffled_cards()
        return self.cards.pop()


# deck = Deck()
# drawn = []
# for _ in range(52):
#     drawn.append(deck.draw())

# count_rank_5 = sum([1 for card in drawn if card.rank == 5])
# count_hearts = sum([1 for card in drawn if card.suit == "Hearts"])

# print(count_rank_5 == 4)  # True
# print(count_hearts == 13)  # True

# drawn2 = []
# for _ in range(52):
#     drawn2.append(deck.draw())

# print(drawn != drawn2)  # True (Almost always).

# In the previous two exercises, you developed a Card class and a Deck class. You are now going to use those classes to create and evaluate poker hands. Create a class, PokerHand, that takes 5 cards from a Deck of Cards and evaluates those cards as a poker hand.
# Include Card and Deck classes from the last two exercises.

from collections import Counter


class PokerHand:
    HAND_SIZE = 5

    def __init__(self, deck):
        self.hand = [deck.draw() for _ in range(PokerHand.HAND_SIZE)]

    def print(self):
        for idx in range(PokerHand.HAND_SIZE):
            print(self.hand[idx])

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
            return "High card"

    def _is_royal_flush(self):
        suits = set()
        ranks = set()
        for card in self.hand:
            ranks.add(card.rank)
            suits.add(card.suit)
        if len(suits) != 1:
            return False
        return ranks == {"Ace", "King", "Queen", "Jack", 10}

    def _is_straight_flush(self):
        suits = set()
        for card in self.hand:
            suits.add(card.suit)

        if len(suits) != 1:
            return False

        sorted_hand = sorted(self.hand)
        for idx, card in enumerate(sorted_hand):
            next_card_value = sorted_hand[idx + 1].value
            if (card.value + 1) != next_card_value:
                return False
            if idx == len(sorted_hand) - 2:
                return True

    def _is_four_of_a_kind(self):
        rank_counter = Counter(card.rank for card in self.hand)
        return 4 in rank_counter.values()

    def _is_full_house(self):
        rank_counter = Counter(card.rank for card in self.hand)
        return 3 in rank_counter.values() and 2 in rank_counter.values()

    def _is_flush(self):
        suit_counter = Counter(card.suit for card in self.hand)
        return 5 in suit_counter.values()

    def _is_straight(self):
        sorted_hand = sorted(self.hand)
        for idx, card in enumerate(sorted_hand):
            next_card_value = sorted_hand[idx + 1].value
            if (card.value + 1) != next_card_value:
                return False
            if idx == len(sorted_hand) - 2:
                return True

    def _is_three_of_a_kind(self):
        rank_counter = Counter(card.rank for card in self.hand)
        return 3 in rank_counter.values()

    def _is_two_pair(self):
        ranks = set(card.rank for card in self.hand)
        return len(ranks) == 3

    def _is_pair(self):
        ranks = set(card.rank for card in self.hand)
        return len(ranks) == 4


# Adding TestDeck class for testing purposes


class TestDeck(Deck):
    def __init__(self, cards):
        self.cards = cards


# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")
