import os

os.system("clear")
# Write a program that asks the user for two numbers and divides the first number by the second number. Handle any potential ZeroDivisionError or ValueError exceptions (there is no need to retry inputs in this problem).
# try:
#     num1 = float(input("Enter number 1: "))
#     num2 = float(input("Enter number 2: "))
#     result = num1 / num2
# except (ValueError, ZeroDivisionError) as e:
#     print(e)
# else:
#     print(result)
# finally:
#     print("End of the program")

# Expand your answer to the previous program so it prints the result only when no exceptions are raised. You should also print End of the program regardless of whether an exception is raised.
# Modify your answer to the previous problem so it handles both ZeroDivisionError and ValueError with a single exception handler. The output for both exception types can be obtained from the exception object.


# Write a program that asks the user for a number. If the input isn't a number, let Python raise an appropriate exception. If the number is negative, raise a ValueError with an appropriate error message. If the number isn't negative, print a message that shows its value.
class NegativeNumberError(ValueError):
    pass


# num = float(input("Enter a number: "))
# if num < 0:
#     raise NegativeNumberError("Number can not be negative")
# print(f"You entered {num}")

# Modify your answer from the previous problem to raise a custom exception named NegativeNumberError instead of an ordinary ValueError exception.


# Write a function that takes a list of numbers and returns the inverse of each number (if n is a number, then 1 / n is its inverse). Handle any exceptions that might occur.
def inverse_num(numbers: list):
    try:
        return [1 / num for num in numbers]
    except TypeError:
        print("Elements in the list must be numeric types")
    except ZeroDivisionError:
        print("Elements in list can not contain 0")


# print(inverse_num([1, 2, 3, 4]))
# print(inverse_num([1, 2, 3, 0]))

# Which of the following code snippets would raise a ZeroDivisionError?
# a) 5 / 2
# b) 3 // 0
# c) 8 % (1 - 1)
# d) 7 / (3 + 4)
# B, C

# Given the following global dictionary:
students = {"John": 25, "Jane": 22, "Doe": 30}


# Write a Python function get_age(name) that takes a student's name as an argument and returns their age. If the student's name isn't in the dictionary, the function should return 'Student not found'.
def get_age(name):
    try:
        return students[name]
    except KeyError:
        return "Student not found"


# print(get_age("John"))
# print(get_age("Jon"))

# Given the following list:
numbers = [1, 2, 3, 4, 5]


# Write two functions to fetch the sixth element from the list: one using the LBYL approach and another using the AFNP approach. In both cases, the function should return None when the element isn't found.
def lbyl_num(num_list):
    if len(num_list) < 6:
        return None
    return num_list[5]


def afnp_num(num_list):
    try:
        return num_list[5]
    except IndexError:
        return None


# Which of the following code snippets would raise an AttributeError?
# a) 'hello'.upper()
# b) [1, 2, 3].push(4)
# c) {'key': 'value'}.get('key')
# d) (12345).length()
# B, D
