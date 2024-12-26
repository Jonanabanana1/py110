# Our countdown to launch isn't behaving as expected. Why? Change the code so that our program successfully counts down from 10 to 1 before launching.
# def decrease(counter):
#     return counter - 1
# counter = 10
# for _ in range(10):
#     print(counter)
#     counter = decrease(counter)
# print('LAUNCH!')

# You have a function that is supposed to reverse a string passed as an argument. However, it's not producing the expected output. Explain the bug, and provide a solution.
# def reverse_string(string):
#     for char in string:
#         string = char + string
#     return string
# print(reverse_string("hello") == "olleh")
# # The following bug is a logical bug. In each iteration of the for loop, the variable string is reassigned to a string object containing the result of adding the first character of string to the beginning of string. The intention is that as you iterate through the loop, because you are adding the characters to the beginning of the string object, it results in a reversed list. But the original string still remains at the end. To fix this instead of setting string = char + string, you should Initalize a new string variable that initially references an empty string. That way you don't have the end wacky bit.
# def reverse_string(string):
#     new_string = ''
#     for char in string:
#         new_string = char + new_string
#     return new_string
# print(reverse_string("hello") == "olleh")

# # You want to multiply all elements of a list by 2. However, the function is not returning the expected result. Explain the bug, and provide a solution.
# def multiply_list(lst):
#     for item in lst:
#         item *= 2

#     return lst
# print(multiply_list([1, 2, 3]) == [2, 4, 6])
# # The item variable referenced in the for loop is a separate reference to the list object's values. Both the list object value and item have a reference to the same object, but when you reassign item, the list object still references the original object, while item has now been reassigned to another object entirely.

# # You have a function that should check whether a key exists in a dictionary and returns its value. However, it's raising an error. Why is that? How would you fix this code?
# def get_key_value(my_dict, key):
#     if my_dict[key]:
#         return my_dict[key]
#     else:
#         return None

# print(get_key_value({"a": 1}, "b"))
# # If you attempt to reference a key in a dictionary that does not exist, a KeyError will be raised. Instead you can use .get() and if a key does not exist, a default value will be returned instead. Alternatively you could try to catch the exception yourself using a try except block

# # We have a list of events and want to check whether a specific date is available (i.e., no events planned for that date). However, the function always returns the wrong value.
# events = {
#     "2023-08-13": ["Python debugging exercises"],
#     "2023-08-14": ["Read 'Automate the Boring Stuff'"],
#     "2023-08-15": ["Webinar: Python for Data Science"],
# }
# def is_date_available(date):
#     if date in events:
#         return True

#     return False
# print(is_date_available("2023-08-14"))  # should return False
# print(is_date_available("2023-08-16"))  # should return True
# # This is a logic bug. Currently is_date_available checks if a date is in the events dictionary and if it is, it returns true else false. What we wants is to to check the opposite so simply reverse true and false

# We want to create a function that appends a given value to a list. However, the function seems to be behaving unexpectedly:
# def append_to_list(value, lst=[]):
#     lst.append(value)
#     return lst

# print(append_to_list(1) == [1])
# print(append_to_list(2) == [2])
# # The bug lies in the fact that we initialize lst to a list object and in the function mutate that list object. For the first function call the list object now holds [1], and for the second function call the list object now holds [1,2]. If instead we wanted to create a separate list object each time the function is called, instead of setting a default parameter lst, make it a positional parameter, and initialize lst in the body with an if statement that lst is None

# # We defined a function intending to multiply the sum of numbers by a factor. However, the function raises an error. Why? How would you fix this code?
# def sum(numbers, factor):
#     return factor * sum(numbers)

# numbers = [1, 2, 3, 4]
# print(sum(numbers, 2) == 20)
# # The issue is that the local user defined function of sum overrides python's bulit in sum function. So when you invoke sum(numbers) python instead invokes the user defined function of sum that takes two parameters, not one, and thus raises an error. To fix this just rename the user defined sum function.

# # We have a list of lists and want to duplicate it. After making the copy, we modify the original list, but the copied list also seems to be affected:
# import copy

# original = [[1], [2], [3]]
# copied = copy.copy(original)

# original[0][0] = 99

# print(copied[0] == [1])
# The issue is that using the .copy method creates a shallow copy of the original object. This means that if within the original object, there are references to mutable objects, those references will also be copied over and will share the same references with the newly created copy. So when you reassign the inner mutable object in the copied list, the same change will appear in the original object.

# We want to remove certain items from a set while iterating over it, but the code below throws an error. Why is that and how can we fix it?
# data_set = {1, 2, 3, 4, 5}

# for item in data_set:
#     if item % 2 == 0:
#         data_set.remove(item)
# The code raises an error as the size of the set changed while you're iterating over it. Python does not allow this and so to fix it you can create a copy of dataset and remove the elements from the copy while iterating over the original.

# A developer is trying to remove duplicates from a list. They use a set for deduplication, but the order of elements is lost. How can we preserve the order?
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed
# You can use the in keyword to create a new list while keeping the same order
