import os
os.system('clear')
# Given a dictionary where both keys and values are unique, invert this dictionary so that its keys become values and its values become keys.
# def invert_dict(map: dict):
#     keys = list(map.keys())
#     values = list(map.values())
#     return dict(zip(values, keys))
#     # return {value: key for key, value in map.items()}
# print(invert_dict({
#           'apple': 'fruit',
#           'broccoli': 'vegetable',
#           'salmon': 'fish',
#       }) == {
#           'fruit': 'apple',
#           'vegetable': 'broccoli',
#           'fish': 'salmon',
#       })  # True

# Given a dictionary and a list of keys, produce a new dictionary that only contains the key/value pairs for the specified keys.
# def keep_keys(map: dict, key_list: list):
#     return {key: value for key, value in map.items() if key in key_list}
# input_dict = {
#     'red': 1,
#     'green': 2,
#     'blue': 3,
#     'yellow': 4,
# }

# keys = ['red', 'blue']
# expected_dict = {'red': 1, 'blue': 3}
# print(keep_keys(input_dict, keys) == expected_dict) # True

# Write a function that takes a list of strings and returns a list of the same string values, but with all vowels (a, e, i, o, u) removed.
# def remove_vowels(string_list: list[str]):
#     consonant_strings = []
#     for string in string_list:
#         cleaned_string = ''
#         for char in string:
#             if char.lower() in ('a', 'e', 'i', 'o', 'u'):
#                 continue
#             cleaned_string += char
#         consonant_strings.append(cleaned_string)
#     return consonant_strings

# # All of these examples should print True
# original = ['abcdefghijklmnopqrstuvwxyz']
# expected = ['bcdfghjklmnpqrstvwxyz']
# print(remove_vowels(original) == expected)        # True

# original = ['green', 'YELLOW', 'black', 'white']
# expected = ['grn', 'YLLW', 'blck', 'wht']
# print(remove_vowels(original) == expected)        # True

# original = ['ABC', 'AEIOU', 'XYZ']
# expected = ['BC', '', 'XYZ']
# print(remove_vowels(original) == expected)        # True

# Write a function that takes a string as an argument and returns a list that contains every word from the string, with each word followed by a space and the word's length. If the argument is an empty string or if no argument is passed, the function should return an empty list.
# You may assume that every pair of words in the string will be separated by a single space.

# def get_word_length(word: str):
#     return f'{word} {len(word)}'
# def word_lengths(string: str = ''):
#     word_list = string.split()
#     return [get_word_length(word) for word in word_list]
# # All of these examples should print True
# words = 'cow sheep chicken'
# expected_result = ['cow 3', 'sheep 5', 'chicken 7']
# print(word_lengths(words) == expected_result)        # True
# words = 'baseball hot dogs and apple pie'
# expected_result = ['baseball 8', 'hot 3', 'dogs 4',
#                    'and 3', 'apple 5', 'pie 3']
# print(word_lengths(words) == expected_result)        # True
# words = "It ain't easy, is it?"
# expected_result = ['It 2', "ain't 5", 'easy, 5',
#                    'is 2', 'it? 3']
# print(word_lengths(words) == expected_result)        # True
# big_word = 'Supercalifragilisticexpialidocious'
# print(word_lengths(big_word) == [f'{big_word} 34'])  # True
# print(word_lengths('') == [])                        # True
# print(word_lengths() == [])                          # True

# Given two lists of integers of the same length, return a new list where each element is the product of the corresponding elements from the two lists.
# def multiply_items(lst1: list, lst2: list):
#     return [num1 * num2 for num1, num2 in zip(lst1, lst2)]

# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
# print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

# Write a function that takes a list of numbers and returns the sum of the sums of each leading subsequence in that list. Examine the examples to see what we mean. You may assume that the list always contains at least one number.
# def sum_of_sums(numbers: list):
#     total_sum = 0
#     for idx in range(1, len(numbers) + 1):
#         total_sum += sum(numbers[:idx])
#     return total_sum
# print(sum_of_sums([3, 5, 2]) == 21)               # True
# # (3) + (3 + 5) + (3 + 5 + 2) --> 21
# print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36
# print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# # (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35
# print(sum_of_sums([4]) == 4)                      # True

# Write a function that takes one argument, a positive integer, and returns the sum of its digits.
# def sum_digits(number: int):
#     digit_int_list = [int(num) for num in str(number)]
#     return sum(digit_int_list)

# print(sum_digits(23) == 5)              # True
# print(sum_digits(496) == 19)            # True
# print(sum_digits(123456789) == 45)      # True

# Write a function that takes a string as an argument and returns that string with a staggered capitalization scheme. Every other character, starting from the first, should be capitalized and should be followed by a lowercase or non-alphabetic character. Non-alphabetic characters should not be changed, but should be counted as characters for determining when to switch between upper and lower case.
# def staggered_case(string: str):
#     staggered_string = ''
#     for idx, char in enumerate(string):
#         func = char.upper if idx % 2 == 0 else char.lower
#         staggered_string += func()
#     return staggered_string

# string = 'I Love Launch School!'
# result = "I LoVe lAuNcH ScHoOl!"
# print(staggered_case(string) == result)  # True
# string = 'ALL_CAPS'
# result = "AlL_CaPs"
# print(staggered_case(string) == result)  # True
# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True
# print(staggered_case('') == "")          # True

# Modify the function from the previous exercise so it ignores non-alphabetic characters when determining whether it should uppercase or lowercase each letter. The non-alphabetic characters should still be included in the return value; they just don't count when toggling the desired case.
# def staggered_case(string: str):
#     staggered_string = ''
#     alpha_index = 0
#     for char in string:
#         func = char.upper if alpha_index % 2 == 0 else char.lower
#         staggered_string += func()
#         if char.isalpha():
#             alpha_index += 1
#     return staggered_string

# string = 'I Love Launch School!'
# result = "I lOvE lAuNcH sChOoL!"
# print(staggered_case(string) == result)  # True
# string = 'ALL_CAPS'
# result = "AlL_cApS"
# print(staggered_case(string) == result)  # True
# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True
# print(staggered_case('') == "")          # True

# Given a sequence of integers, filter out instances where the same value occurs successively, retaining only the initial occurrence. Return the refined sequence.
def unique_sequence(numbers: list):
    previous_number = numbers[0]
    cleaned_numbers = [previous_number]
    for number in numbers:
        if number == previous_number:
            continue
        cleaned_numbers.append(number)
        previous_number = number
    return cleaned_numbers

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True