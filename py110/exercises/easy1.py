import os

os.system("clear")
# Write a program that solicits six (6) numbers from the user and prints a
# message that describes whether the sixth number appears among the first five.
# numbers = []
# for idx in range(5):
#     numbers.append(input("Enter a number: "))
# sixth_number = input("Enter the last number: ")
# if sixth_number in numbers:
#     print(f"{sixth_number} is in {', '.join(numbers)}")

# Write a function that returns True if the string passed as an argument is
# a palindrome, False otherwise. A palindrome reads the same forwards and
# backwards. For this problem, the case matters and all characters matter.

# def is_palindrome(string: str) -> bool:
#     return string == string[::-1]

# # All of these examples should print True
# print(is_palindrome("madam") == True)
# print(is_palindrome("356653") == True)
# print(is_palindrome("356635") == False)
# # case matters
# print(is_palindrome("Madam") == False)
# # all characters matter
# print(is_palindrome("madam i'm adam") == False)

# # Now make a function named is_real_palindrome, but make it case-insensitive
# # and ignore all non-alphanumeric characters
# def is_real_palindrome(string: str) -> bool:
#     case_insensitive_alphanum_str = ""
#     for char in string:
#         if not char.isalnum():
#             continue
#         case_insensitive_alphanum_str += char.casefold()
#     return is_palindrome(case_insensitive_alphanum_str)

# print(is_real_palindrome("madam") == True)  # True
# print(is_real_palindrome("356653") == True)  # True
# print(is_real_palindrome("356635") == False)  # True
# print(is_real_palindrome("356a653") == True)  # True
# print(is_real_palindrome("123ab321") == False)  # True

# # case doesn't matter
# print(is_real_palindrome("Madam") == True)  # True

# # only alphanumerics matter
# print(is_real_palindrome("Madam, I'm Adam") == True)  # True


# Write a function that takes a list and returns a new list that represents
# the running total of the original list.
# def running_total(numbers):
#     total = 0
#     new_numbers = []
#     for number in numbers:
#         new_numbers.append(total + number)
#         total += number
#     return new_numbers

# print(running_total([2, 5, 13]) == [2, 7, 20])  # True
# print(running_total([14, 11, 7, 15, 20]) == [14, 25, 32, 47, 67])  # True
# print(running_total([3]) == [3])  # True
# print(running_total([]) == [])  # True


# Write a function that takes a string of 0 or more space separated words
# and returns a dictionary that shows the number of words of different sizes
# All of these examples should print True
# def word_sizes(string):
#     word_dictionary = {}
#     string_words = string.split()
#     for word in string_words:
#         word_dictionary.setdefault(len(word), 0)
#         word_dictionary[len(word)] += 1
#     return word_dictionary

# string = "Four score and seven."
# print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})
# string = "Hey diddle diddle, the cat and the fiddle!"
# print(word_sizes(string) == {3: 5, 6: 1, 7: 2})
# string = "Humpty Dumpty sat on a wall"
# print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})
# string = "What's up doc?"
# print(word_sizes(string) == {6: 1, 2: 1, 4: 1})
# print(word_sizes("") == {})


# Modify the word_sizes function such that it excludes non alpha characters
# from being included in the word size. Ex It's == 3 not 4
# def word_sizes(string):
#     word_dictionary = {}
#     string_words = string.split()
#     cleaned_words = []
#     cleaned_word = ""
#     for word in string_words:
#         for char in word:
#             if not char.isalpha():
#                 continue
#             cleaned_word += char
#         cleaned_words.append(cleaned_word)
#         cleaned_word = ""

#     for word in cleaned_words:
#         word_dictionary.setdefault(len(word), 0)
#         word_dictionary[len(word)] += 1
#     return word_dictionary


# # All of these examples should print True
# string = "Four score and seven."
# print(word_sizes(string) == {4: 1, 5: 2, 3: 1})
# string = "Hey diddle diddle, the cat and the fiddle!"
# print(word_sizes(string) == {3: 5, 6: 3})
# string = "Humpty Dumpty sat on a w@ll"
# print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})
# string = "What's up doc?"
# print(word_sizes(string) == {5: 1, 2: 1, 3: 1})
# print(word_sizes("") == {})


# Write a function that takes in a string and returns a new string with
# the first and last letters of each word swapped.
# def swap_word(string: str):
#     if len(string) <= 2:
#         return string[::-1]
#     new_word = string[-1] + string[1 : len(string) - 1] + string[0]
#     return new_word

# def swap(string):
#     word_list = string.split()
#     reversed_list = [swap_word(word) for word in word_list]
#     return " ".join(reversed_list)

# print(
#     swap("Oh what a wonderful day it is") == "hO thaw a londerfuw yad ti si"
# )  # True
# print(swap("Abcde") == "ebcdA")  # True
# print(swap("a") == "a")  # True


# Convert a string to an integer without using any built in python type
# conversion functions
# def string_to_integer(string: str):
#     string = string[::-1]
#     sum = 0
#     multiples_of_ten = 1
#     for char in string:
#         sum += (ord(char) - 48) * multiples_of_ten
#         multiples_of_ten *= 10
#     return sum


# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570") == 570)  # True


# # Optional: Write a hexadecimal_to_integer function. Hexadecimal is base 16
# # with A B C D E F == 10 11 12 13 14 15 respectively
# def hexadecimal_to_integer(string: str):
#     hexadecimal_map = {
#         "0": 0,
#         "1": 1,
#         "2": 2,
#         "3": 3,
#         "4": 4,
#         "5": 5,
#         "6": 6,
#         "7": 7,
#         "8": 8,
#         "9": 9,
#         "a": 10,
#         "b": 11,
#         "c": 12,
#         "d": 13,
#         "e": 14,
#         "f": 15,
#         "A": 10,
#         "B": 11,
#         "C": 12,
#         "D": 13,
#         "E": 14,
#         "F": 15,
#     }
#     # 4D9f, f = 15 * 16^0
#     #       9 = 9 * 16^1
#     sum = 0
#     power_16 = len(string) - 1
#     for char in string:
#         sum += hexadecimal_map[char] * pow(16, power_16)
#         power_16 -= 1
#     return sum
# print(hexadecimal_to_integer("4D9f") == 19871)  # True


# Convert a string to an integer but this time account for signs. If there
# are not signs treat it as a positive number.
# def string_to_signed_integer(string: str):
#     string = string[::-1]
#     sum = 0
#     multiples_of_ten = 1
#     sign = 1
#     for char in string:
#         if char == "+":
#             continue
#         elif char == "-":
#             sign = -1
#             continue
#         sum += (ord(char) - 48) * multiples_of_ten
#         multiples_of_ten *= 10
#     return sum * sign


# print(string_to_signed_integer("4321") == 4321)  # True
# print(string_to_signed_integer("-570") == -570)  # True
# print(string_to_signed_integer("+100") == 100)  # True


# Now write a function that takes a positive integer and converts
# it to a string. You can't use built in conversion functions
def integer_to_string(number: int) -> str:
    # Divmod() returns a tuple (a // b, a % b)
    string_map = {
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        0: "0",
    }
    string_num = ""
    while number > 0:
        number, remainder = divmod(number, 10)
        string_num = string_map[remainder] + string_num
    return string_num or "0"


print(integer_to_string(4321) == "4321")  # True
print(integer_to_string(0) == "0")  # True
print(integer_to_string(5000) == "5000")  # True
print(integer_to_string(1234567890) == "1234567890")  # True


# Now write a function that accepts signed numbers
def signed_integer_to_string(number: int):
    if number > 0:
        return "+" + integer_to_string(number)
    if number < 0:
        return "-" + integer_to_string(-number)
    return "0"


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")  # True
print(signed_integer_to_string(0) == "0")  # True
