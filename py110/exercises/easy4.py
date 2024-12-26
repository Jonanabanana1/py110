import os
os.system('clear')
# Write a function that takes a list of integers between 0 and 19 and returns a list of those integers sorted based on the English word for each number:
# def alphabetic_number_sort(num_list: list):
    # return sorted(num_list, key=number_to_english)

# def number_to_english(number: int):
#     english_map = {
#         0: 'zero',
#         1: 'one',
#         2: 'two',
#         3: 'three',
#         4: 'four',
#         5: 'five',
#         6: 'six',
#         7: 'seven',
#         8: 'eight',
#         9: 'nine',
#         10: 'ten',
#         11: 'eleven',
#         12: 'twelve',
#         13: 'thirteen',
#         14: 'fourteen',
#         15: 'fifteen',
#         16: 'sixteen',
#         17: 'seventeen',
#         18: 'eightteen',
#         19: 'nineteen'
#     }
#     return english_map[number]

# input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#               10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
#                    7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

# print(alphabetic_number_sort(input_list) == expected_result)
# # Prints True

# Given two lists, convert them to sets and return a new set which is the union of both sets.
# def merge_sets(lst1, lst2):
#     return set(lst1) | set(lst2)
# list1 = [3, 5, 7, 9]
# list2 = [5, 7, 11, 13]
# print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# # Prints True

# Transform two lists into frozen sets and find their common elements.
# def intersection(lst1, lst2):
#     return frozenset(lst1) & frozenset(lst2)
# list1 = [2, 4, 6, 8]
# list2 = [1, 3, 5, 7, 8]
# expected_result = frozenset({8})
# print(intersection(list1, list2) == expected_result) # True

# Given a dictionary, return its keys sorted by the values associated with each key.
# def order_by_value(dictionary):
#     return sorted(dictionary.keys(), key=dictionary.get)

# my_dict = {'p': 8, 'q': 2, 'r': 6}
# keys = ['q', 'r', 'p']
# print(order_by_value(my_dict) == keys)  # True

# From two list arguments, determine the elements that are unique to the first list. The return value should be a set.
# def unique_from_first(lst1, lst2):
#     return set(lst1) - set(lst2)
# list1 = [3, 6, 9, 12]
# list2 = [6, 12, 15, 18]
# print(unique_from_first(list1, list2) == {9, 3})

# # Write a function that takes a string argument and returns a list of substrings of that string. Each substring should begin with the first letter of the word, and the list should be ordered from shortest to longest.
# # All of these examples should print True
# def leading_substrings(string: str):
#     substrings = []
#     for idx in range(1, len(string) + 1):
#         substrings.append(string[0:idx])
#     return substrings
# # print(leading_substrings('abc') == ['a', 'ab', 'abc'])
# # print(leading_substrings('a') == ['a'])
# # print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

# # Write a function that returns a list of all substrings of a string. Order the returned list by where in the string the substring begins. This means that all substrings that start at index position 0 should come first, then all substrings that start at index position 1, and so on. Since multiple substrings will occur at each position, return the substrings at a given index from shortest to longest.
# def substrings(string: str):
#     total_substrings = []
#     for idx in range(len(string)):
#         total_substrings.extend(leading_substrings(string[idx:]))
#     return total_substrings
# # expected_result = [
# #     "a", "ab", "abc", "abcd", "abcde",
# #     "b", "bc", "bcd", "bcde",
# #     "c", "cd", "cde",
# #     "d", "de",
# #     "e",
# # ]
# # print(substrings('abcde') == expected_result)  # True

# # Write a function that returns a list of all palindromic substrings of a string. That is, each substring must consist of a sequence of characters that reads the same forward and backward. The substrings in the returned list should be sorted by their order of appearance in the input string. Duplicate substrings should be included multiple times.
# # You may (and should) use the substrings function you wrote in the previous exercise.
# # For the purpose of this exercise, you should consider all characters and pay attention to case; that is, 'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are not. In addition, assume that single characters are not palindromes.
# def is_palindrome(string: str):
#     if len(string) <= 1:
#         return False
#     return string == string[::-1]

# def palindromes(string: str):
#     palindrome_list = [substring for substring in substrings(string) if is_palindrome(substring)]
#     return palindrome_list
# print(palindromes('madam'))
# print(palindromes('abcd') == [])                  # True
# print(palindromes('madam') == ['madam', 'ada'])   # True
# print(palindromes('hello-madam-did-madam-goodbye') ==
#                   [
#                       'll', '-madam-', '-madam-did-madam-',
#                       'madam', 'madam-did-madam', 'ada',
#                       'adam-did-mada', 'dam-did-mad',
#                       'am-did-ma', 'm-did-m', '-did-',
#                       'did', '-madam-', 'madam', 'ada', 'oo',
#                   ])    # True
# print(palindromes('knitting cassettes') ==
#                   [
#                       'nittin', 'itti', 'tt', 'ss',
#                       'settes', 'ette', 'tt',
#                   ])    # True

# Write a function that takes two arguments, an inventory item ID and a list of transactions, and returns a list containing only the transactions for the specified inventory item.
def correct_transaction(item_ID, transaction):
    return transaction["id"] == item_ID
def transactions_for(item_ID: int, transaction_list: list):
    return [transaction for transaction in transaction_list if correct_transaction(item_ID, transaction)]
transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]
# print(transactions_for(101, transactions) ==
#       [
#           {"id": 101, "movement": "in",  "quantity":  5},
#           {"id": 101, "movement": "in",  "quantity": 12},
#           {"id": 101, "movement": "out", "quantity": 18},
# ]) # True
# Building on the previous exercise, write a function that returns True or False based on whether or not an inventory item (an ID number) is available. As before, the function takes two arguments: an item ID and a list of transactions. The function should return True only if the sum of the quantity values of the item's transactions is greater than zero. Notice that there is a movement property in each transaction object. A movement value of 'out' will decrease the item's quantity.
def is_item_available(item_id, transaction_list):
    filtered_transactions = transactions_for(item_id, transaction_list)
    sum = 0
    for transaction in filtered_transactions:
        if transaction['movement'] == 'in':
            sum += transaction['quantity']
        else:
            sum -= transaction['quantity']
    return sum > 0
print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True