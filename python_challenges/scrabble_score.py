"""
Write a program that, given a word, computes the Scrabble score for that word.

Requirements:
    - Create a class named Scrabble
    - Contains a method named score() that returns an int representing scrabble score
    - case insensitive scoring
    - None scores 0
    - Empty string scores 0
    - Whitespace only score 0

Point Values
A, E, I, O, U, L, N, R, S, T 	1
D, G 	                        2
B, C, M, P 	                    3
F, H, V, W, Y 	                4
K 	                            5
J, X 	                        8
Q, Z 	                        10


"""


class Scrabble:
    point_values = {
        "a": 1,
        "e": 1,
        "i": 1,
        "o": 1,
        "u": 1,
        "l": 1,
        "n": 1,
        "r": 1,
        "s": 1,
        "t": 1,
        "d": 2,
        "g": 2,
        "b": 3,
        "c": 3,
        "m": 3,
        "p": 3,
        "f": 4,
        "h": 4,
        "v": 4,
        "w": 4,
        "y": 4,
        "k": 5,
        "j": 8,
        "x": 8,
        "q": 10,
        "z": 10,
    }

    def __init__(self, word: str) -> None:
        if not isinstance(word, str):
            if word is not None:
                raise TypeError("Word must be either type None or a string")
            word = ""

        self.word = word.strip().lower()

    @classmethod
    def calculate_score(cls, word: str) -> int:
        if not word:
            return 0

        sum = 0
        for letter in word:
            sum += cls.point_values.get(letter, 0)
        return sum

    def score(self) -> int:
        return Scrabble.calculate_score(self.word)
