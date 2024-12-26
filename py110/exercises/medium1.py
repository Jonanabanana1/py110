import sys
sys.set_int_max_str_digits(50_000)
import os
import string
os.system('clear')
# Write a function that rotates a list by moving the first element to the end of the list. Do not modify the original list; return a new list instead.
# If the input is an empty list, return an empty list.
# If the input is not a list, return None.

# def rotate_list(lst: list):
#     if type(lst) is not list:
#         return None
#     if len(lst) < 2:
#         return lst
#     new_list = lst[1:] + [lst[0]]
#     return new_list

# print(rotate_list([7, 3, 5, 2, 9, 1]))
# # All of these examples should print True
# print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
# print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
# print(rotate_list(['a']) == ['a'])
# print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
# print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
# print(rotate_list([]) == [])

# # return `None` if the argument is not a list
# print(rotate_list(None) == None)
# print(rotate_list(1) == None)

# # the input list is not mutated
# lst = [1, 2, 3, 4]
# print(rotate_list(lst) == [2, 3, 4, 1])
# print(lst == [1, 2, 3, 4])

# Write a function that rotates the last count digits of a number. To perform the rotation, move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.
# '''
# input: number: int, count: int
# output: number: int
# Requirements:
#     - Return a number with its last `count` digits rotated
#     - To rotate, take the left most digit as specified from count and move it to the end of the number. Then shift the rest of the numbers to the left.
#     - If count is 1 or less, return the same number
# Algorithm:
#     - Convert input number to string and then into a list to get digits
#     - Remove the count digit
#     - Append the count digit to the end
#     - Use str.join to turn back into string and then int() fin
# '''
# def rotate_rightmost_digits(number: int, count: int):
#     digits = list(str(number))
#     count_digit = digits.pop(-count)
#     digits.append(count_digit)
#     return int(''.join(digits))

# # Take the number 735291 and rotate it by one digit to the left, getting 352917. Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. Keep the first two digits fixed in place and rotate again to get 321759. Keep the first three digits fixed in place and rotate again to get 321597. Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. The resulting number is called the maximum rotation of the original number.
# # Write a function that takes an integer as an argument and returns the maximum rotation of that integer. You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.
# '''
# Requirements:
#     - Return a number with count - 1 rotations
# Algorithm:
#     - Rotate number, then use the result and rotate that.
#     - Rotate for a total for count - 1
# '''
# def max_rotation(number: int):
#     number_of_digits = len(str(number))
#     bruh = -number_of_digits
#     for _ in range(number_of_digits - 1):
#         number = rotate_rightmost_digits(number, -bruh)
#         bruh += 1
#     return number

# print(max_rotation(735291) == 321579)          # True
# print(max_rotation(3) == 3)                    # True
# print(max_rotation(35) == 53)                  # True
# print(max_rotation(8703529146) == 7321609845)  # True

# # Note that the final sequence here is `015`. The leading
# # zero gets dropped, though, since we're working with
# # an integer.
# print(max_rotation(105) == 15)                 # True

# Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.
# You may assume that the string does not contain any punctuation.
# '''
# Algorithm:
#     - Split string into words and store words in a list
#     - Check if a word is a number word
#     - If so, replace the number word with the number
#     - Join back the words
# '''
# NUMBER_WORDS = {
#     'one': '1',
#     'two': '2',
#     'three': '3',
#     'four': '4',
#     'five': '5',
#     'six': '6',
#     'seven': '7',
#     'eight': '8',
#     'nine': '9',
# }
# def word_to_digit(text: str):
#     words = text.split()
#     for idx, word in enumerate(words):
#         if word[-1] in string.punctuation:
#             if word[:-1] in NUMBER_WORDS:
#                 words[idx] = NUMBER_WORDS[word[:-1]] + word[-1]
#         elif word in NUMBER_WORDS:
#             words[idx] = NUMBER_WORDS[word]
#     return ' '.join(words)

# # message = 'Please call me at five five five one two three four'
# # print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# # Should print True
# # Can you solve this problem if the individual words can end with punctuation? For instance:
# message = 'Please call me at five, five, five, one, two, three, four.'
# print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# # Should print True
    
# A prime number is a positive number that is evenly divisible only by itself and 1. Thus, 23 is prime since its only divisors are 1 and 23. However, 24 is not prime since it has divisors of 1, 2, 3, 4, 6, 8, 12, and 24. Note that the number 1 is not prime.
# Write a function that takes a positive integer as an argument and returns true if the number is prime, false if it is not prime.
# '''
# Algorithm:
#     - Iterate over the range up to number
#     - Check if number % idx is 0
#     - If it is, that means it is evenly divisible so return false
#     - Else return true
# '''
# def is_prime(num: int):
#     if num < 2:
#         return False
#     for idx in range(2, num):
#         if num % idx == 0:
#             return False
#     return True
# print(is_prime(1) == False)              # True
# print(is_prime(2) == True)               # True
# print(is_prime(3) == True)               # True
# print(is_prime(4) == False)              # True
# print(is_prime(5) == True)               # True
# print(is_prime(6) == False)              # True
# print(is_prime(7) == True)               # True
# print(is_prime(8) == False)              # True
# print(is_prime(9) == False)              # True
# print(is_prime(10) == False)             # True
# print(is_prime(23) == True)              # True
# print(is_prime(24) == False)             # True
# print(is_prime(997) == True)             # True
# print(is_prime(998) == False)            # True
# print(is_prime(3_297_061) == True)       # True
# print(is_prime(23_297_061) == False)     # True

# The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers. The first two Fibonacci numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:
# F(1) = 1
# F(2) = 1
# F(n) = F(n - 1) + F(n - 2)    (where n > 2)
# Write a function called fibonacci that computes the nth Fibonacci number, where nth is an argument passed to the function:
'''
Algorithm:
    - If num is less than or equal to 2, return 1
    - We can calc any fib(n) by calc fib(3) which we know is 2
    - To calc fib 4, thats fib 3 + fib 2 which is 1.
    - Each time we calc a fib, update the values of the fib previous
    - Continue this until we calc fib(n) by having fib(n-1) and fib(n-2)
'''
# def fibonacci(num: int):
#     if num <= 2:
#         return 1
#     fib_1 = 1
#     fib_2 = 1
#     fib_index = 2
#     while fib_index < num:
#         fib_next = fib_1 + fib_2
#         fib_2 = fib_1
#         fib_1 = fib_next
#         fib_index += 1
#     return fib_next
# Now make it use memoization to save memory and have it be recursive
# fib_seen = {}
# def fibonacci(num: int):
#     if num <= 2:
#         return 1
#     elif num in fib_seen:
#         return fib_seen[num]
#     else:
#         fib_seen[num] = fibonacci(num-1) + fibonacci(num - 2)
#         return fib_seen[num]

# print(fibonacci(4))
# print(fibonacci(1) == 1)                  # True
# print(fibonacci(2) == 1)                  # True
# print(fibonacci(3) == 2)                  # True
# print(fibonacci(4) == 3)                  # True
# print(fibonacci(5) == 5)                  # True
# print(fibonacci(6) == 8)                  # True
# print(fibonacci(12) == 144)               # True
# print(fibonacci(20) == 6765)              # True
# print(fibonacci(50) == 12586269025)       # True
# print(fibonacci(75) == 2111485077978050)  # True
# Now make it use memoization to save memory and have it be recursive
fib_seen = {}
def fibonacci(num: int):
    if num <= 2:
        return 1
    elif num in fib_seen:
        return fib_seen[num]
    else:
        fib_seen[num] = fibonacci(num-1) + fibonacci(num - 2)
        return fib_seen[num]
def find_fibonacci_index_by_length(digits: int):
    nth = 2
    while True:
        fib_string = str(fibonacci(nth))
        if len(fib_string) == digits:
            break
        nth += 1
    return nth
# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)