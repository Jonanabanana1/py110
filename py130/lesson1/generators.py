import os

os.system("clear")

# Create a generator expression that generates the reciprocals of the numbers from 1 to 10. A reciprocal of a number n is 1 / n. Use a for loop to print each value.
# reciprocals = (1 / number for number in range(1, 11))
# for number in reciprocals:
#     print(number)


# Create a generator function that generates the reciprocals of the numbers from 1 to n, where n is an argument to the function. Use a for loop to print each value.
# def gen_recipriocals(max):
#     start = 1
#     while start <= max:
#         yield 1 / start
#         start += 1

# for number in gen_recipriocals(7):
#     print(number)

# Use a generator expression to capitalize every string in a list of strings. Use a single print invocation to print all the capitalized strings as a tuple.
# strings = ["hi", "my", "name"]
# print(tuple(text.capitalize() for text in strings))


# Create a generator function that generates the capitalized version of every string in a list of strings. Use a single print invocation to print all the capitalized strings as a tuple.
# def cap_strings(strings):
#     for string in strings:
#         yield string.capitalize()


# print(tuple(cap_strings(["yo", "wassup", "hows it going"])))


# Use a generator expression to capitalize the strings in a list of strings whose length is at least 5. Use a single print invocation to print all the capitalized strings as a set.
strings = ["hi", "wassupdude", "yooooooo", "not"]
# print(set(string.capitalize() for string in strings if len(string) >= 5))


# Create a generator function that generates the capitalized version of every string in a list of strings whose length is less than 5. Use a single print invocation to print all the capitalized strings as a set.
def cap_strings_with_length_5(strings):
    for string in strings:
        if len(string) >= 5:
            yield string.capitalize()


print(set(cap_strings_with_length_5(strings)))

# print(set(cap_string(strings)))
