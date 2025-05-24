import os

os.system("clear")


# What will the following code print?
# def make_greeting():
#     greeting = "Hello"

#     def greet_func(name, greet=None):
#         if not greet:
#             return f"{greeting} {name}!"

#         return f"{greet} {name}!"

#     return greet_func


# greet_person = make_greeting()
# print(greet_person("John", "Goodbye"))
# print(greet_person("Jane"))


# def make_counter():
#     def counter_func():
#         counter = 0
#         counter += 1
#         return counter

#     return counter_func


# increment_counter = make_counter()
# print(increment_counter())
# print(increment_counter())

# increment_counter = make_counter()
# print(increment_counter())
# print(increment_counter())


# from functools import partial


# def greet(name, greeting):
#     return f"{greeting}, {name}!"


# say_hello_to = partial(greet, greeting="Hello")
# print(say_hello_to(name="Alice"))  # What will this print?


# Write a function named later that takes two arguments: a function, func, and an argument for that function, argument. The return value should be a new function that calls func with argument as its argument. Here's an example of how it might be used:
# def later(func, argument):
#     return lambda: func(argument)


# def printer(message):
#     print(message)


# print_warning = later(printer, "The system is shutting down!")
# print_warning()  # The system is shutting down!


# Write a function named later2 that takes two arguments: a function, func, and an argument for that function, first_arg. The return value should be a new function that takes an argument, second_arg. The new function should call the func with the arguments provided by first_arg and second_arg. Here's an example of how it might be used:
def later2(func, first_arg):
    def inner(second_arg):
        func(first_arg, second_arg)

    return inner


def notify(message, when):
    print(f"{message} in {when} minutes!")


shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30)  # The system is shutting down in 30 minutes!
