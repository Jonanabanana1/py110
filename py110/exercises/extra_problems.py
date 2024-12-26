import os

os.system("clear")
"""
Create a function that takes a list of numbers as an argument. For each number, determine how many numbers in the list are smaller than it, and place the answer in a list. Return the resulting list.

When counting numbers, only count unique values. That is, if a number occurs multiple times in the list, it should only be counted once.

Input: list of numbers
Output: New list with each element representing the amount of elements smaller than the current element in the original list

Requirements:
    - Input list is not mutated
    - A list with one element will return [0]
    - If all elements are the same, return a new list with the same amount of elements but that are all 0
    - Only count unique values, if a number appears more than once, it should only be counted once.
    - For each number, determine how many unique numbers are smaller than it in the resulting list. 
    - Must compare all numbers regardless of their position in the list, i.e. the last element should also be checked with the beginning elements.

Algorithm:
    1) Iterate through each element in the input list
    2) Check if current element is less than other elements in the list
        - Have 2 loops, one iterating for the length of the input list which will ensure every element gets compared
        - Inner loop will be the one in which the index at the outer loop is being compared with the other elements
        - If the outer index and inner index equal to each other, then skip as there's no need to check the same element
    3) If so, increment a counter variable, and after checking every element add the counter variable to a new list.
        - Only increment counter variable if the element being checked is a unique value. To determine uniqueness I can create a list that will hold all elements already checked and see if the current element is in that list.
        - Initialize the seen list at the outer loop, to ensure the seen list gets refreshed after checking each outer element.
"""


def smaller_numbers_than_current(numbers: list[int]) -> list[int]:
    result = []
    for num in numbers:
        less_than_counter = 0
        seen_number = []
        for other_num in numbers:
            if num == other_num or other_num in seen_number:
                continue
            if num > other_num:
                less_than_counter += 1
            seen_number.append(other_num)
        result.append(less_than_counter)

    return result


"""
Create a function that takes a list of integers as an argument. The function should return the minimum sum of 5 consecutive numbers in the list. If the list contains fewer than 5 elements, the function should return None.

Input: list of integers
Output: None if list contains less than 5 elements, otherwise minimum sum of 5 consecutive numbers in list

Requirements:
    - If length of list is less than 5, return None
    - Consecutive numbers mean they have to be after each other in order
    - Must return the lowest sum possible from 5 consecutive numbers in the list

Ideas:
    - If length of list less than 5, return None
    - Check every combination of possible 5 consecutive numbers
    - First check first 5, then increment idx to check next 5 elements.
    - Keep going until you reach the end.
    - Keep track of a global min

Algorithm:
    1) If length of list is less than 5 return None
    2) Set min equal to sum of first possible 5 numbers in list
    3) Increment idx in list in terms of start and end to grab next 5 consecutive numbers. Use slicing to grab five
    4) If sum from current 5 elements is lower than min, set min equal to that sum.
    5) Keep going until you reach the end
    6) Return the minimum sum
"""


def minimum_sum(numbers: list[int]):
    num_length = len(numbers)
    if num_length < 5:
        return None
    end_index = 5
    start_index = 0

    min = sum(numbers[start_index:end_index])
    while end_index <= num_length:
        current_sum = sum(numbers[start_index:end_index])
        if current_sum < min:
            min = current_sum
        start_index += 1
        end_index += 1
    return min


"""
Create a function that takes a string argument and returns a copy of the string with every second character in every third word converted to uppercase. Other characters should remain the same.

Input: string
Output: Copy of input string but with every second character in third word converted to uppercase. Other characters are the same.

Requirements:
    - Every third word, every even character in the word must be capitalized
    - If the third word only has 1 character, nothing happens

Algorithm:
    - Split the input string into a list of words
    - Iterate through the list, checking every 3rd element
    - Every third element, replace the string inside with a new string
    - New string should have every even character uppercased
        - Create a new empty string
        - Iterate through idx of length of string
        - Check if idx % 2 == 0 to see if it is a even character
        - If even, append uppercased character
        - If odd, append normal character
        - Once done iterating through string, replace string with new string
    - Join the elements in the list together and return string
"""


def to_weird_case(string: str) -> str:
    words = string.split()
    for idx, word in enumerate(words):
        if (idx + 1) % 3 != 0:
            continue
        new_word = ""
        for char_idx, char in enumerate(word):
            if (char_idx + 1) % 2 == 0:
                new_word += char.upper()
            else:
                new_word += char
        words[idx] = new_word
    return " ".join(words)


"""
Create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value. If there are multiple pairs that are equally close, return the pair that occurs first in the list.

P:
    Input: list of integers
    Output: tuple of two numbers closest together in value
    Requiments:
        - If there are mutliple pairs that are equally close, return the first pair that occurs first in the input list
        - Pairs don't have to be directly next to each other
    
D:
    min_difference = 0
    min_pair = None

Algorithm:
    Iterate through input list
    Grab pair of numbers and find thier difference
        - Use two loops, outer loop compares each number. Outer loop should start at first index and end at last index
        - Inner loop, comparing numbers to other numbers after it. Inner loop will start at the idx of outer loop, and end at the length of the list.
    If the difference is lower than min_difference, set min different = to the difference and set the tuple pair as the pair value
"""


def closest_numbers(numbers: list) -> tuple | None:
    min_difference = abs(numbers[0] - numbers[1])
    min_pair = None
    if len(numbers) < 2:
        return None
    for outer_idx in range(len(numbers)):
        for inner_idx in range(outer_idx, len(numbers) - 1):
            pair = (numbers[outer_idx], numbers[inner_idx + 1])
            if abs(pair[0] - pair[1]) < min_difference:
                min_difference = abs(pair[0] - pair[1])
                min_pair = pair
    return min_pair


"""
Create a function that takes a string argument and returns the character that occurs most often in the string. If there are multiple characters with the same greatest frequency, return the one that appears first in the string. When counting characters, consider uppercase and lowercase versions to be the same.

Input: string argument
Output: character that occurs most often in the string

Requirements:
    - If there are characters with the same greatest frequency, return the one that appears first in the input string
    - Characters should be case insensitive
    - Return value for the character with the most occurance should be in lowercase

Ideas:
    - Iterate through the string
    - Dictionary to keep track of amount of occurances per letter
        Key: Letter (lowercase) Value: Amount of time it appears in string
    - To check for greatest amount in dictionary, I can iterate through the dictionary's key value items, set max to the highest value.

Algorithm:
    - Initialize an empty dictionary representing the # of occurances per letter
    - Iterate through the string per character
    - For each character I can add the lower-cased version of the character to the dictionary. If the key already exists, increment the value by 1, otherwise create a new key with the value of 1
        - For each character I can use dict.setdefault(0) to intialize if it doesnt exist. And then always increment the value
    - Initialize a max occurance value to 0
    - Initialize a max_key to None
    - Iterate through dictionary key - value pairs
    - If value at key is greater than max occurance
        - Set max occurance to value at key
        - Set max_key to key
    - Return max key
"""


def most_common_char(string: str) -> str | None:
    letter_occurances = {}
    for char in string:
        letter_occurances.setdefault(char.lower(), 0)
        letter_occurances[char.lower()] += 1
    max_occurances = 0
    max_key = None
    for key, value in letter_occurances.items():
        if value > max_occurances:
            max_occurances = value
            max_key = key
    return max_key


"""
Create a function that takes a string argument and returns a dict object in which the keys represent the lowercase letters in the string, and the values represent how often the corresponding letter occurs in the string.

Input: string argument
Output: dict object
    - Keys: lowercase letter in the string
    - Values: integer representing how often the key occurs in the string

Requirements:
    - Only add alphabetical characters to the dictionary object
    - Only lowercase alphabetical characters are considered
    - Return an empty dictionary if the input string is empty

Ideas:
    - Iterate through each character in the input string
    - If the character is alphabetical and lowercased
        - Add the character as the key to the dictionary if the key does not already exist. Set the value to 1
        - If the key does exist, increment the value at the key
    - Return the dictionary object
"""


def count_letters(string: str) -> dict:
    result = {}
    for char in string:
        if not char.isalpha() or char.isupper():
            continue
        result[char] = result.get(char, 0) + 1
    return result


"""
Create a function that takes a list of integers as an argument and returns the number of identical pairs of integers in that list. For instance, the number of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice, count each complete pair once. For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should return 2. The first list contains two complete pairs while the second has an extra 2 that isn't part of the other two pairs.

Input: list of integers
Output : int # of identical pairs of integers in that list.

Requirements:
    - If the length of the list is less than or equal to 1, return 0
    - If a number occurs more than once, count each pair once
    - A pair consists of two identical numbers
    - If there are 3 of the same numbers, that only makes 1 pair

Question:
    Shoud the input list be mutated?
Ideas:
    Sort the list from ascending order
    Iterate through the list
    Check if current index is equal to next index
    If so I know its a pair
    Increment a pair counter
    If its not a pair, increment current index by 1.
    Increment current index by 2 instead of one to not double check
    Repeat checking process
    Once the next index is equal to the last index of the list, stop checking and return the value of the pair counter
"""
from collections import Counter


def pairs(numbers: list[int]) -> int:
    if len(numbers) <= 1:
        return 0
    num_counts = Counter(numbers)
    pair_amount = sum([count // 2 for count in num_counts.values()])
    return pair_amount


"""
Create a function that takes a non-empty string as an argument. The string consists entirely of lowercase alphabetic characters. The function should return the length of the longest vowel substring. The vowels of interest are "a", "e", "i", "o", and "u".

Input: Non-empty string. Entirely made up of lowercase alpha characters
Output: int: length of the longest vowel substring

Requirements:
    - Vowels: 'a', 'e', 'i', 'o', 'u'
    - A substring must be a countinuous chain of characters one after the other
    - If there are no vowels return 0

Ideas:
    - I could iterate through the string and once I see a vowel, I start keeping count of how many vowels are after it
    - Once I meet a non vowel character, I save the number of vowels into a max_vowels variable and repeat the process.
    - If another vowel chain appears, check if the length of the vowel chain is greater than max_vowels, if so, set max_vowels to new vowel chain

Algorithm:
    - Initialize a vowel_counter to 0
    - Initialize a max_vowels to 0
    - Iterate through each character in the string
    - If the character is a vowel:
        - Increment vowel_counter
    - If the character is not a vowel:
        - Check if vowel_counter is greater than max_vowels:
            - If so, set max_vowels equal to vowel_counter
        - Set vowel_counter to 0
    - Once you're done with the string, check if vowel_counter is greater than max_vowels in case the ending contains vowels
    - Return max_vowels
"""


def longest_vowel_substring(string: str) -> int:
    vowels = {"a", "e", "i", "o", "u"}
    max_vowels = 0
    current_vowels = 0
    for char in string:
        if char in vowels:
            current_vowels += 1
            max_vowels = max(max_vowels, current_vowels)
        else:
            current_vowels = 0
    return max_vowels


"""
Create a function that takes two string arguments and returns the number of times that the second string occurs in the first string. Note that overlapping strings don't count: 'babab' contains 1 instance of 'bab', not 2.

You may assume that the second argument is never an empty string.

Input: 2 String arguments
Output: Int: Number of times second string occurs in first string

Requirements:
    Overlapping strings should not be counted
    Second argument is never an empty string
    If first argument is an empty string, return 0
    All strings will be in lowercase

Ideas:
    I could use the count method for strings
"""


def count_substrings(str1, str2):
    return str1.count(str2)


"""
Create a function that takes a string of digits as an argument and returns the number of even-numbered substrings that can be formed. For example, in the case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a separate substring.

Input: string: digits
Output: int: number of even-numbered substrings that can be formed

Examples: '1432' -> '14', '1432', '4', '432', '32', '2'

Requirements:
    - Even numbered substrings means that the value of the string when converted to a number must be divisible by 2
    - If a substring occurs more than once, count each occurance as a separate substring

Ideas:
    - Need to create a list of all possible substrings
        - Use a for loop to iterate through each character
        - Use an inner loop which will be one character ahead of the outer loop
        - Inside of the inner loop I can create a substring of the input string starting from outer_index to inner_index (inclusive)
        - Add substring to list
    - Convert each element in list to a number
    - Check if the number is even and increment counter if so
    - Return counter

Algorithm:
    1) Create an empty list named substrings
    2) Iterate through each character in input string
    3) Inside of the loop, create another loop starting one index ahead of the outer loop
        - Outer loop should end at len(string) - 1, because we are adding 1 later to account for idx
    4) Use python's slicing to create a substring of the input string starting from outer_indx to inner_indx + 1 to account for exclusive end parameter
    5) Convert substring to a number and add number to substrings list
    6) Iterate through substrings list, incrementing counter variable if number in substrings % 2 == 0
    7) Return counter variable
"""


def even_substrings(num_string: str) -> int:
    substrings = []
    for outer_idx in range(len(num_string)):
        for inner_idx in range(outer_idx, len(num_string)):
            substring = num_string[outer_idx : inner_idx + 1]
            substrings.append(int(substring))

    even_counter = 0
    for num in substrings:
        if num % 2 == 0:
            even_counter += 1

    return even_counter


"""
Create a function that takes a nonempty string as an argument and returns a tuple consisting of a string and an integer. If we call the string argument s, the string component of the returned tuple t, and the integer component of the tuple k, then s, t, and k must be related to each other such that s == t * k. The values of t and k should be the shortest possible substring and the largest possible repeat count that satisfies this equation.

You may assume that the string argument consists entirely of lowercase alphabetic letters.

Input: Non-empty string
Output: tuple, first element is a string second is an integer

Examples:
Input string = s
Tuple string = t
Tuple integer = k

s == t * k

Requirements:
    - The tuple string should be the shortest possible substring
    - The tuple integer should the largest possible repeat value

Ideas:
    Find the multiples in which a possible repeating substring can occur
        Grab the length of the string
        Check which numbers from 1 to length of the string that the length can be divided by evenly. 
        Save the divisors in which the length divides evenly with 0 remainders in a list.
    Grab the substring from index 0 to multiple - 1 (0 index) and multiply by number necessary to reach length of string. If the resulting outcome matches, return the substring and integer.
    Otherwise move on to next possible divisor and repeat

Algorithm:
    Initialize string_length to length of string
    Initialize divisor_list to empty list
    Iterate from 1 to string_length checking if string_length % index is equal to 0. If so, append index to divisor list
    
    Iterate through divisor_list in the reverse order
    Divide length of string by current element to find multiple
    Check if string[0:element] * multiple is equal to the input string
    If so, return a tuple consisting of the substring and multiple

"""


def repeated_substring(string: str) -> tuple:
    string_length = len(string)
    divisor_list = []
    for idx in range(1, string_length + 1):
        if string_length % idx == 0:
            divisor_list.append(idx)

    for divisor in divisor_list:
        multiple = string_length // divisor
        substring = string[0:divisor]
        if substring * multiple == string:
            return (substring, multiple)
    raise Exception


"""
Create a function that takes a string as an argument and returns True if the string is a pangram, False if it is not.

Pangrams are sentences that contain every letter of the alphabet at least once. For example, the sentence "Five quacking zephyrs jolt my wax bed." is a pangram since it uses every letter at least once. Note that case is irrelevant.

Input: string
Output: boolean, True if input is a pangram, False if not

Pangrams:
    - Sentences that contain every letter of the alphabet at least once.
    - Case is irrelevant

Ideas:
    - Use a set
    - Add each character in the input string to the set
    - Check if the set contains all the letters of the alphabet

Algorithm:
    1) Initialize a alphabet set to empty
    2) Iterate through the input string
    3) Add the current character in lowercase to the set
    4) Check if the set is equal to a set that contains all lowercase letters of the alphabet

"""

import string


def is_pangram(my_string: str) -> bool:
    return set(string.ascii_lowercase).issubset(set(my_string))


"""
Create a function that takes two strings as arguments and returns True if some portion of the characters in the first string can be rearranged to match the characters in the second. Otherwise, the function should return False.

You may assume that both string arguments only contain lowercase alphabetic characters. Neither string will be empty.

Input: two strings
Output: bool representing if characters in first string can be rearranged to match second string

Requirements:
    - Both string arguments only contain lowercase alpha characters
    - Neither string will be empty

Ideas:
    - Use a counter object to count the amount of times a letter appears in a string. 
    - Compare counter objects for equality between the two input strings
"""


def unscramble(str1, str2):
    str1_counter = Counter(str1)
    str2_counter = Counter(str2)
    str1_counter.subtract(str2_counter)
    for value in str1_counter.values():
        if value < 0:
            return False
    return True


"""
Create a function that takes a single integer argument and returns the sum of all the multiples of 7 or 11 that are less than the argument. If a number is a multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. The sum of these multiples is 75.

If the argument is negative, return 0.

Input: single integer argument
Output: the sum of all multiples of 7 OR 11 that are LESS than the input.

Examples:
    Input: 25
    Output: 7 + 11 + 14 + 21 + 22 = 75

Requirements:
    - If a number is a multiple of both 7 and 11, count it once for the sum.
    - If input is less than or equal to 0, return 0

Ideas:
    Use two ranges each incrementing by 7 or 11 and appending the values to a set to sum up

Algorithm:
    1) Iterate through a range starting from 7 up to input but not including and the step value is 7
    2) Do the same but for 11
    3) While you're iterating add the value to a set
    4) Sum up the values in the set and return the sum
"""


def seven_eleven(number: int) -> int:
    return sum(num for num in range(number) if num % 7 == 0 or num % 11 == 0)


"""
Create a function that takes a string argument that consists entirely of numeric digits and computes the greatest product of four consecutive digits in the string. The argument will always have more than 4 digits.

Input: string consisting of only integer numbers
Output: integer representing greatest product of 4 consecutive digits in the string

Requirements:
    - The argument will always have more than 4 digits
    - The digits have to be next to each other to be considered consecutive

Ideas:
    1) Take a slice from index 0 to but not including 4 to grab first 4 elements. Take the product of those digits and store it as the max sum.
    Then I could go to the next 4 digits and compute the product, compare against the max sum and eventually return the max sum
    
Algorithm:
    1) Declare a starting index to 0 and ending index to 4
    2) Take a slice from starting index to ending index out of the input string
    3) Convert the substring to a list contianing each character as an integer element
    4) Compute the product of the digits in the list.
    5) Set max_product equal to whichever product is greater
    6) Increment starting and ending index
    7 Repeat steps 2-6 until ending index is equal to length of input string
"""
import math


def greatest_product(num_str: str) -> int:
    max_product = 0
    start_idx = 0
    end_idx = 4
    while end_idx <= len(num_str):
        four_digit_slice = slice(start_idx, end_idx)
        current_substring = num_str[four_digit_slice]
        num_list = [int(char) for char in current_substring]
        current_product = math.prod(num_list)
        max_product = max(max_product, current_product)
        start_idx, end_idx = start_idx + 1, end_idx + 1
    return max_product


"""
Create a function that returns the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. You may assume that the input string contains only alphanumeric characters.

Input: string containing only alphanumeric characters
Output: integer representing the count of distinct case-insensitive alphabetic characters AND numeric digits that occur MORE than once in the input string

Requirements:
    - Output should count DISTINCT:
        - Case insensitive alphabetic characters
        - numeric digits
        - APPEAR MORE THAN ONCE
    - If there are multiple instances of the same character, that character is only counted once towards the output

Ideas:
    - Dictionary to keep track of the number of times a distinct character has appeared
    - Counter dictionary 
    - Convert the string to lowercase
    - Create a list consisting of keys that have a value of 2 or more
    - Return the length of the list

Algorithm:
    - Convert string to lowercase
    - Create a counter dictionary with the string as the argument
    - Create a list consisting of only keys that have a value of 2 or more
    - Return the length of the list
"""


def distinct_multiples(string: str) -> int:
    string = string.lower()
    unique_counter = Counter(string)
    return sum(count > 1 for count in unique_counter.values())


"""
Create a function that takes a list of integers as an argument. The function should determine the minimum integer value that can be appended to the list so the sum of all the elements equal the closest prime number that is greater than the current sum of the numbers. For example, the numbers in [1, 2, 3] sum to 6. The nearest prime number greater than 6 is 7. Thus, we can add 1 to the list to sum to 7.

    The list will always contain at least 2 integers.
    All values in the list must be positive (> 0).
    There may be multiple occurrences of the various numbers in the list.

Input: list of integers
Output: Integer value

Input: [1, 2, 3] -> Closest prime to sum: 6 is 7. Output: 1 
Requirements:
    - Output should be the minimum integer value that can be appended to the input list such that:
        - The sum of all the elements equals the closest prime number
        - The closest prime number must be greater than the current sum of the numbers
    - The input list will always contain at least 2 integers
    - All values in input lists are positive
    - Numbers in lists can be the same

Ideas:
    - Need to determine the next closest prime number after the sum of the input list
    - A prime number is a number that is only divisible by itself and 1
    - I can first find the sum, check the next closest number to see if its a prime number
    - I can check from prime by running a range and seeing if any numbers up to the number is divisible and has a remainder of 0

Algorithm:
    - Find the sum of the input list
    - Set next_prime equal to the sum + 1
    - Check if next_prime is a prime number
    - If not, increment next_prime and repeat
    - Once a match is found, subtract next_prime and sum of input_list and return the difference

"""

prime_numbers = set()


def is_prime(num):
    if num in prime_numbers:
        return True
    for idx in range(2, num):
        if num % idx == 0:
            return False
    prime_numbers.add(num)
    return True


def nearest_prime_sum(numbers: list) -> int:
    num_sum = sum(numbers)
    next_prime = num_sum + 1
    while True:
        if is_prime(next_prime):
            return next_prime - num_sum
        next_prime += 1


print(nearest_prime_sum([1, 2, 3]) == 1)  # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)  # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)  # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5)  # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)
