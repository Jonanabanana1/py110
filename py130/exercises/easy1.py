import os

os.system("clear")
# Create a list where each number from the original list is squared using the map method.
# original = [1, 2, 3, 4]
# new = list(map(lambda num: num**2, original))
# print(new)

# Obtain only the even numbers from a list using the filter function.
# original = [1, 2, 3, 4]
# new = list(filter(lambda num: num % 2 == 0, original))
# print(new)

# Calculate the product of all numbers in a list using the reduce function.
# from functools import reduce

# original = [2, 2, 3, 4]
# product = reduce(lambda number, accum: accum * number, original)
# print(product)

# Use map to create a list of lengths of each string in the original list.
# original = ["hello", "my", "name", "is", "timothy"]
# new = list(map(len, original))
# print(new)

# Remove all None values from a list using the filter method.
# original = [1, None, 4, 5, None, 3]
# new = list(filter(lambda x: x is not None, original))
# print(new)

# Use reduce to concatenate a list of strings into a single string.
# from functools import reduce

# strings = ["hey", "i", "just", "met", "you"]
# print(reduce(lambda accum, string: accum + string, strings))

# Use nested generator expressions to create a flat list of numbers from a list of lists.
# nested_numbers = [[1, 2, 3], [4, 5, 6]]
# numbers = (num for inner_lst in nested_numbers for num in inner_lst)
# print(list(numbers))

# Use a generator expression to yield each character of a string in reverse order.
# my_str = "abcdefg"
# rev_str = (char for char in my_str[::-1])
# for char in rev_str:
#     print(char)


# Create a generator function that yields numbers from 1 to 5.
# def gen_num():
#     for num in range(1, 6):
#         yield num


# for num in gen_num():
#     print(num)


# Create a generator function that yields user input strings until the word "stop" is entered.
def gen_input():
    while True:
        user_input = input("Enter stop to quit: ")
        if user_input == "stop":
            break
        yield user_input


for user_input in gen_input():
    print(user_input)
