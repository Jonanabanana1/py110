import os

os.system("clear")


# Create a function greet that takes three arguments: a name, a greeting, and a punctuation mark, with the punctuation defaulting to a period.
def greet(name, greeting, punctuation="."):
    return f"{greeting}, {name}{punctuation}"


# Create a function create_user that takes a username and requires keyword-only arguments for email and age.
def create_user(username, *, email, age):
    return {"username": username, "email": email, "age": age}


# Write a function build_profile that takes a first name and a last name, and any number of keyword arguments to add to a user's profile.
def build_profile(first_name, last_name, **kwargs):
    user = {"first_name": first_name, "last_name": last_name}
    for name, value in kwargs.items():
        user[name] = value
    return user


# Create a function concatenate that takes any number of strings and concatenates them into a single string with a space in between.
def concatenate(*args):
    return " ".join(args)


# Write a function display_info that takes a positional-only parameter data, and keyword-only parameters reverse and uppercase.
def display_info(data, /, *, reverse=False, uppercase=False):
    if reverse:
        data = data[::-1]
    if uppercase:
        data = data.upper()
    return data


# Given a list with four elements, unpack these elements into four separate variables.
lst = [10, 20, 30, 40]
a, b, c, d = lst

# Unpack values from a tuple of four elements, but only keep the first and last values.
data = (100, 200, 300, 400)
first, *_, last = data

# Unpack the first two elements from a list and store the remaining elements in another list.
numbers = [1, 2, 3, 4, 5, 6]
first, second, *extra = numbers

# Given a nested tuple data = ((1, 2), (3, 4), (5, 6)), write a code to unpack this tuple into individual variables a, b, c, d, e, f.
data = ((1, 2), (3, 4), (5, 6))
((a, b), (c, d), (e, f)) = data
