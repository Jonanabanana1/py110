import os
os.system('clear')
# The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.
# Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm). Your function should work with any integer input.
# You may not use Python's datetime module.
# MINUTES_IN_HOUR = 60
# def time_of_day(minutes_after_midnight: int):
#     hours, minutes = divmod(abs(minutes_after_midnight), MINUTES_IN_HOUR)
#     while hours >= 24:
#         hours -= 24

#     if minutes_after_midnight < 0:
#         if minutes > 0:
#             hours = 24 - hours - 1
#             minutes = MINUTES_IN_HOUR - minutes
#         else:
#             hours = 24 - hours
    
#     return f'{hours:02}:{minutes:02}'
# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True

# Now do it converting the time to minutes
# def after_midnight(time_after: str):
#     hours = int(time_after[0:2])
#     minutes = int(time_after[3:])
#     if hours == 24:
#         hours = 0
#     return (hours * 60) + minutes
# def before_midnight(time_before: str):
#     hours = int(time_before[0:2])
#     minutes = int(time_before[3:])
#     hours = 24 - hours - 1
#     if minutes > 0:
#         minutes = 60 - minutes
#     else:
#         hours += 1
#     if hours == 24:
#         return 0
#     return (hours * 60) + minutes

# print(after_midnight("00:00") == 0)     # True
# print(before_midnight("00:00") == 0)    # True
# print(after_midnight("12:34") == 754)   # True
# print(before_midnight("12:34") == 686)  # True
# print(after_midnight("24:00") == 0)     # True
# print(before_midnight("24:00") == 0)    # True

# Write a function that takes a string, doubles every character in the string, then returns the result as a new string.
# def repeater(string: str):
#     doubled_characters = [char * 2 for char in string]
#     return ''.join(doubled_characters)
# print(repeater('Hello') == "HHeelllloo")              # True
# print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
# print(repeater('') == "")                             # True

# Now Write the repeater function but for only consonants
# def double_consonants(string: str):
#     vowels = ('a', 'e', 'i', 'o', 'u')
#     double_string = ''
#     for char in string:
#         if char.lower() in vowels or not char.isalpha():
#             double_string += char
#         else:
#             double_string += char * 2
#     return double_string
# # All of these examples should print True
# print(double_consonants('String'))
# print(double_consonants('String') == "SSttrrinngg")
# print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
# print(double_consonants('July 4th') == "JJullyy 4tthh")
# print(double_consonants('') == "")

# Write a function that takes a positive integer as an argument and returns that number with its digits reversed.
# def reverse_number(number):
#     return int(str(number)[::-1])

# print(reverse_number(12345) == 54321)   # True
# print(reverse_number(12213) == 31221)   # True
# print(reverse_number(456) == 654)       # True
# print(reverse_number(1) == 1)           # True
# print(reverse_number(12000) == 21)      # True

# Write a function that takes an integer argument and returns a list containing all integers between 1 and the argument (inclusive), in ascending order.
# def sequence(number: int):
#     return list(range(1, number + 1))
# print(sequence(5) == [1, 2, 3, 4, 5])   # True
# print(sequence(3) == [1, 2, 3])         # True
# print(sequence(1) == [1])               # True

# Write a function that takes a string argument consisting of a first name, a space, and a last name. The function should return a new string consisting of the last name, a comma, a space, and the first name.
# def swap_name(name: str):
#     first, last = name.split()
#     return f'{last}, {first}'
# print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

# Create a function that takes two integers as arguments. The first argument is a count, and the second is the starting number of a sequence that your function will create. The function should return a list containing the same number of elements as the count argument. The value of each element should be a multiple of the starting number.
# def sequence(count: int, start: int):
#     return [start * idx for idx in range(1, count + 1)]

# print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
# print(sequence(4, -7) == [-7, -14, -21, -28])     # True
# print(sequence(3, 0) == [0, 0, 0])                # True
# print(sequence(0, 1000000) == [])                 # True

# Write a function that takes a list as an argument and reverses its elements, in place. That is, mutate the list passed into the function. The returned object should be the same object used as the argument.
# You may not use the list.reverse method nor may you use a slice ([::-1]).
# def reverse_list(lst: list):
#     swap_amount = len(lst) // 2
#     start_index = 0
#     end_index = -1
#     for _ in range(swap_amount):
#         temp = lst[end_index]
#         lst[end_index] = lst[start_index]
#         lst[start_index] = temp
#         start_index += 1
#         end_index -= 1
#     return lst
    
# list1 = [1, 2, 3, 4]
# result = reverse_list(list1)
# print(result == [4, 3, 2, 1])               # True
# print(list1 is result)                      # True
# list2 = ["a", "b", "c", "d", "e"]
# result2 = reverse_list(list2)
# print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
# print(list2 is result2)                     # True
# list3 = ["abc"]
# result3 = reverse_list(list3)
# print(result3 == ['abc'])                   # True
# print(list3 is result3)                     # True
# list4 = []
# result4 = reverse_list(list4)
# print(result4 == [])                        # True
# print(list4 is result4)                     # True

# Write a function that takes a string as an argument and returns True if all parentheses in the string are properly balanced, False otherwise. To be properly balanced, parentheses must occur in matching '(' and ')' pairs.
def is_balanced(string: str):
    open_paren_count = 0
    close_paren_count = 0
    for char in string:
        if char == ')':
            close_paren_count += 1
        elif char == '(':
            open_paren_count += 1
        if close_paren_count > open_paren_count:
            return False
    return open_paren_count == close_paren_count
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True