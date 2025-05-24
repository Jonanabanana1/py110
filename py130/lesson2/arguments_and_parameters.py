import os

os.system("clear")


# Write a function named combine that takes three positional arguments and returns a tuple containing all three. Call this function with three different values.
# def combine(a, b, c, /):
#     return (a, b, c)


# print(combine(1, "a", 23.2))


# Define a function named multiply that accepts two positional-only arguments and returns their product. The function should not allow these parameters to be passed as keyword arguments.
# def multiply(a, b, /):
#     return a * b


# print(multiply(a=4, b=2))


# Create a function named describe_pet that takes one positional argument animal_type and one keyword argument name with a default value of an empty string. The function should print a description of the pet. The function should not accept more than 1 positional argument.
# def describe_pet(animal_type, *, name=""):
#     print(f"Your pet {name} is a {animal_type}")


# describe_pet("Labrador", name="John")
# describe_pet(animal_type="Labrador", name="John")


# Write a function named calculate_average that any number of numeric arguments and returns their average. Make sure it returns None if no arguments are provided.
def calculate_average(*args):
    return sum(args) / len(args) if args else None


# Create a function named find_person that accepts any number of keyword arguments in which each key is someone's name and the value is their associated profession. The function should check whether any of the key/value pairs has a key of "Antonina" and then, if the key is found, print a message that shows Antonina's profession. Otherwise, it should say "Antonina not found". The function should not accept any positional arguments.
def find_person(**kwargs):
    for name, profession in kwargs.items():
        if name == "Antonina":
            print(f"{name}'s profession is {profession}")
            return
    print("Antonina not found")


# Define a function named concat_strings that takes any number of strings and returns the concatenation of all the strings. Add a keyword-only argument sep with a default value of ' ' that specifies the separator to use between the strings.
# def concat_strings(*strings, sep=" "):
#     return sep.join(strings)


# print(concat_strings("hi", "my", "name", "is"))


# Create a function named register that takes exactly three arguments: username as positional-only, password as keyword-only, and age as either a positional or keyword argument.
def register(username, /, age, *, password):
    pass


# Create a function named print_message that requires a keyword-only argument (message) and an optional keyword-only argument (level) with a default value of "INFO". The function should print out the message prefixed with the level. The function shouldn't accept any positional arguments.
def print_message(*, message, level="INFO"):
    print(level, message)


def something(a, b=None):
    if not b:
        return f"Hi {a}"
    return f"{b} {a}"


print(something("Tim", "Hello"))
