# 1) Compute and display the total age of the family's male members. Try working out the answer two ways: first with an ordinary loop, then with a comprehension.
# munsters = {
#     "Herman": {"age": 32, "gender": "male"},
#     "Lily": {"age": 30, "gender": "female"},
#     "Grandpa": {"age": 402, "gender": "male"},
#     "Eddie": {"age": 10, "gender": "male"},
#     "Marilyn": {"age": 23, "gender": "female"},
# }


# list_male_ages = [info["age"] for info in munsters.values() if info["gender"] == "male"]
# print(sum(list_male_ages))

# 3) Given the following data structure, return a new list with the same structure, but with the values in each sublist ordered in ascending order. Use a comprehension if you can. (Try using a for loop first.)
# lst = [["b", "c", "a"], [2, 11, -3], ["blue", "black", "green"]]
# new_lst = [sorted(sub_list) for sub_list in lst]
# print(new_lst)

# 4) Given the following data structure, write some code that defines a dictionary where the key is the first item in each sublist, and the value is the second.
# lst = [["a", 1], ["b", "two"], ["sea", {"c": 3}], ["D", ["a", "b", "c"]]]
# lst_dict = {sublist[0]: sublist[1] for sublist in lst}
# print(lst_dict)

# 5) Given the following data structure, sort the list so that the sub-lists are ordered based on the sum of the odd numbers that they contain. You shouldn't mutate the original list.
# lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
# def sum_odd_numbers(numbers):
# return sum([number for number in numbers if number % 2 == 1])
# print(sorted(lst, key=sum_odd_numbers))

# 6) Given the following data structure, return a new list identical in structure to the original but, with each number incremented by 1. Do not modify the original data structure. Use a comprehension.
# lst = [{"a": 1}, {"b": 2, "c": 3}, {"d": 4, "e": 5, "f": 6}]
# lst2 = [{key: value + 1 for key, value in sub_dict.items()} for sub_dict in lst]
# print(lst2)

# 7) Given the following data structure return a new list identical in structure to the original, but containing only the numbers that are multiples of 3.
# lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
# lst2 = [[number for number in sublist if number % 3 == 0] for sublist in lst]
# print(lst2)

# 8) Given the following data structure, write some code to return a list that contains the colors of the fruits and the sizes of the vegetables. The sizes should be uppercase, and the colors should be capitalized.
# dict1 = {
#     "grape": {
#         "type": "fruit",
#         "colors": ["red", "green"],
#         "size": "small",
#     },
#     "carrot": {
#         "type": "vegetable",
#         "colors": ["orange"],
#         "size": "medium",
#     },
#     "apricot": {
#         "type": "fruit",
#         "colors": ["orange"],
#         "size": "medium",
#     },
#     "marrow": {
#         "type": "vegetable",
#         "colors": ["green"],
#         "size": "large",
#     },
# }
# dict2 = []
# for value in dict1.values():
#     if value["type"] == "fruit":
#         dict2.append([color.capitalize() for color in value["colors"]])
#     else:
#         dict2.append(value["size"].upper())
# print(dict2)

# 9) This problem may prove challenging. Try it, but don't stress about it. If you don't solve it in 20 minutes, you can look at the answer.
# Given the following data structure, write some code to return a list that contains only the dictionaries where all the numbers are even.
# Iterate through lst
# Iterate through dictionary values
# Iterate through list of numbers
# Check if value in list of numbers is odd
# If number is odd, Dont return dictionary
# If after loop is done successfully Add Dictionary
# lst = [
#     {"a": [1, 2, 3]},
#     {"b": [2, 4, 6], "c": [3, 6], "d": [4]},
#     {"e": [8], "f": [6, 10]},
# ]

# def even_dictionary(dictionary):
#     for num_list in dictionary.values():
#         for number in num_list:
#             if number % 2 != 0:
#                 return None
#     return dictionary

# even_lst = [
#     even_dictionary(sub_dict)
#     for sub_dict in lst
#     if even_dictionary(sub_dict) is not None
# ]
# print(even_lst)

# Cleaner solution
# def all_even(dictionary):
#     for values in dictionary.values():
#         if not all([num % 2 == 0 for num in values]):
#             return False

#     return True
# result = [val for val in lst if all_even(val)]
# print(result)

# 10) Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the letters a-f) represented as a string. The value is typically broken into 5 sections in an 8-4-4-4-12 pattern, e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'
# Write a function that takes no arguments and returns a string that contains a UUID.
# Create a list of numbers representing pattern [8, 4, 4, 4, 12]
# Import Random
# Create method that generates a random string from possible characters that accepts number from list of numbers as its parameter.
# Method should return a string, use that string to build a list
# Join elements in the list separating them with -
# import random

# NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# LETTERS = ["a", "b", "c", "d", "e", "f"]
# POSSIBLE_CHARACTERS = NUMBERS + LETTERS


# def uuid_generator():
#     pattern = [8, 4, 4, 4, 12]
#     uuid = []
#     for number in pattern:
#         uuid.append(unique_string(number))
#     return "-".join(uuid)


# def unique_string(length):
#     string = ""
#     for _ in range(length):
#         string += str(random.choice(POSSIBLE_CHARACTERS))
#     return string


# print(uuid_generator())

# 11) The following dictionary has list values that contains strings. Write some code to create a list of every vowel (a, e, i, o, u) that appears in the contained strings, then print it.
dict1 = {
    "first": ["the", "quick"],
    "second": ["brown", "fox"],
    "third": ["jumped"],
    "fourth": ["over", "the", "lazy", "dog"],
}

# Your code goes here
# Iterate through dict1 list values
# Iterate through element in list
# Iterate through each letter in string
# Check if the letter is a vowel
# If so, append it to vowel_list
VOWELS = ["a", "e", "i", "o", "u"]
list_of_vowels = [
    letter
    for list_value in dict1.values()
    for element in list_value
    for letter in element
    if letter in VOWELS
]
print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
