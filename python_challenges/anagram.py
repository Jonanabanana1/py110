"""
P: Write a class named Anagram that contains an instance method, match, that accepts a list of strings and returns a list containing only the strings that are anagrams to the original anagram word.

Valid Anagrams:
    - Same words do not count
    - Detector should be case insensitive

Ideas:
    - Determine how many occurances of each letter is in the original string
    - Have a dictionary that maps each letter with the number of times it occurs in the string
    - Do that for both the original string and the comparing string and compare dictionaries for equality.

Creating a dictionary that maps each letter with number of times it occurs
    1) Create an empty dictionary named letter_counter
    2) Iterate over each character in the string
    3) If character exists in my_dict as a key, do nothing, else set the character as a new key with a default value of 0
    4) Increment the value of the character key
    5) Repeat for each character in the string

Comparing 2 dictionaries for equality:
    Use == operator, dictionaries compare equality based only if both dictionaries contain the same keys and the keys have equal value regardless of order

"""


class Anagram:
    def __init__(self, word) -> None:
        self.word = word
        self.letter_freq = Anagram.calculate_letter_freq(word)

    @staticmethod
    def calculate_letter_freq(word):
        letter_counter = dict()
        for letter in word.lower():
            letter_counter[letter] = letter_counter.setdefault(letter, 0) + 1
        return letter_counter

    def match(self, strings):
        matching_list = []
        for string in strings:
            if self.word.casefold() == string.casefold():
                continue

            string_letter_count = Anagram.calculate_letter_freq(string)

            if self.letter_freq == string_letter_count:
                matching_list.append(string)

        return matching_list
