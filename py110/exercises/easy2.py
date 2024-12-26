import os

os.system("clear")
# Write a function that takes a floating point number representing an angle between 0 and 360 degrees and returns a string representing that angle in degrees, minutes, and seconds. You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.
# DEGREE = "\u00B0"

# def dms(angle: float) -> str:
#     minutes = (angle % 1) * 60
#     seconds = (minutes % 1) * 60
#     minutes_str = f"{int(minutes):02d}"
#     seconds_str = f"{int(seconds):02d}"
#     return f"{int(angle)}{DEGREE}{minutes_str}'{seconds_str}\""

# # All of these examples should print True
# print(dms(30) == "30°00'00\"")
# print(dms(76.73) == "76°43'48\"")
# print(dms(254.6) == "254°35'59\"")
# print(dms(93.034773) == "93°02'05\"")
# print(dms(0) == "0°00'00\"")
# print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

# Write a function that takes two lists as arguments and returns a set that contains the union of the values from the two lists. You may assume that both arguments will always be lists.
# def union(lst1: list[int], lst2: list[int]):
#     return set(lst1 + lst2)

# print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9})  # True


# Write a function that takes a list as an argument and returns a list that contains two elements, both of which are lists. Put the first half of the original list elements in the first element of the return value and put the second half in the second element. If the original list contains an odd number of elements, place the middle element in the first half list.
# All of these examples should print True
# def halvsies(number_list: list[int]):
#     number_lst_length = len(number_list)
#     middle_index = number_lst_length // 2

#     if number_lst_length % 2 == 1:
#         middle_index += 1

#     left_half = number_list[:middle_index]
#     right_half = number_list[middle_index:]
#     return [left_half, right_half]


# print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
# print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
# print(halvsies([5]) == [[5], []])
# print(halvsies([]) == [[], []])

# Given an unordered list and the information that exactly one value in the list occurs twice (every other value occurs exactly once), determine which value occurs twice. Write a function that finds and returns the duplicate value.
# def find_dup(number_list: list[int]):
#     for number in number_list:
#         if number_list.count(number) > 1:
#             return number
# print(find_dup([1, 5, 3, 1]) == 1) # True
# print(find_dup([
#                   18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
#                   38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
#                   14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
#                   78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
#                   89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
#                   41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
#                   55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
#                   85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
#                   40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
#                    7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
#               ]) == 73)       # True

# Write a function that combines two lists passed as arguments and returns a new list that contains all elements from both list arguments, with each element taken in alternation.
# def interleave(lst1: list, lst2: list):
#     pack = zip(lst1, lst2)
#     return [elem for tup in pack for elem in tup]

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# expected = [1, "a", 2, "b", 3, "c"]
# print(interleave(list1, list2) == expected)      # True

# Write a function that takes a list of positive integers as input, multiplies all of the integers together, divides the result by the number of entries in the list, and returns the result as a string with the value rounded to three decimal places.
# All of these examples should print True
# def multiplicative_average(lst: list):
#     sum = 1
#     for num in lst:
#         sum *= num
#     sum /= len(lst)
#     return f'{sum:.3f}'
# print(multiplicative_average([3, 5]) == "7.500")
# print(multiplicative_average([2, 5, 8]) == "26.667")
# print(multiplicative_average([2, 5]) == "5.000")
# print(multiplicative_average([1, 1, 1, 1]) == "0.250")
# print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

# Write a function that takes two list arguments, each containing a list of numbers, and returns a new list that contains the product of each pair of numbers from the arguments that have the same index. You may assume that the arguments contain the same number of elements.
# def multiply_list(lst1: list, lst2: list):
#     return [num1 * num2 for num1, num2 in zip(lst1, lst2)]

# list1 = [3, 5, 7]
# list2 = [9, 10, 11]
# print(multiply_list(list1, list2) == [27, 50, 77])  # True

# Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.
# def digit_list(number: int):
#     return [int(digit) for digit in str(number)]

# print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
# print(digit_list(7) == [7])                       # True
# print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
# print(digit_list(444) == [4, 4, 4])               # True

# Write a function that counts the number of occurrences of each element in a given list. Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").
# def count_occurrences(lst: list):
#     # For case insensitive
#     lst_lowercase = [element.lower() for element in lst]
#     unique_values = set(lst_lowercase)
#     for value in unique_values:
#         print(f'{value} => {lst_lowercase.count(value)}')

# vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
#             'motorcycle', 'motorcycle', 'car', 'truck']
# count_occurrences(vehicles)

# Write a function that takes one argument, a list of integers, and returns the average of all the integers in the list, rounded down to the integer component of the average. The list will never be empty, and the numbers will always be positive integers.
def average(lst: list):
    return sum(lst) // len(lst)
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True