import os

os.system("clear")
# Write a select function that mimics the built-in filter function. Your select function should take two arguments: a callback function and an iterable object. It should return a list of all the elements of the iterable for which the callback function returns a truthy value. It should not include any elements for which the callback returns a falsy value.


# Start by writing a function that doesn't use any comprehensions. Once your code works, refactor it to use a comprehension.
def select(callback, iterable):
    return [item for item in iterable if callback(item)]


# Write a reject function that mimics the select function you just wrote, but that rejects rather than selects elements from the iterable object. That is, it should return a list of all the elements of the iterable for which the callback function doesn't return a truthy value. It should only include any elements for which the callback returns a falsy value.


# You may use comprehensions if you wish.
def reject(callback, iterable):
    return [item for item in iterable if not callback(item)]


# reduce functions typically take 3 arguments:


#     a callback that takes two arguments. The first argument is the current element of the iterable argument and the second is the current reduction value, commonly called the "accumulator" and named accum.
#     an iterable.
#     a starting value. The starting value is the initial value for the current argument in the callback.
def reduce(callback, iterable, start):
    total = start
    for item in iterable:
        total = callback(item, total)
    return total


numbers = (1, 2, 4, 8, 16)
total = lambda number, accum: accum + number
print(reduce(total, numbers, 0))  # 31

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))  # 300

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
rainbow = lambda color, accum: accum + color[0].upper()
print(reduce(rainbow, colors, ""))  # ROYGBIV

# Use the reduce function shown in the answer to the previous question to compute the sum of the squares in a list of numbers.
numbers = (1, 2, 3, 4)
print(reduce(lambda number, accum: number * number + accum, numbers, 0))
