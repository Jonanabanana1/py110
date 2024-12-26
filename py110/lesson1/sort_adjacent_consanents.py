"""
Given a list of strings, sort the list based on highest number of adjacent consanents in each string. 

Input:
    List of Strings
Output:
    Sorted List of strings

Explicit rules:
    - If 2 strings have the same number of adjacent consanents, the strings should retain their same order in the list in relation to the original list
    - Consonents are considered adjacent if they are next to each other in a word or if separated by a space between words.
Implicit Rules:
    - A consonent by itself does not count as an adjacent consonent
    - A word is considered a sequence of characters not separated by spaces
    - If two strings contain the same amount of adjacent consonents, the string that has a lower index in the original string appears first in the sorted string not matter how far they are separated in terms of indeces
    - Sorted list is sorted in Descending order
Questions:
    - How to treat numbers?
    - Should we account for non-ascii characters?
    - What is considered a word? Does it have to be a word in the english dictionary?
Data Structure:
    Dictionary:
    - Keys: Strings
    - Values: # Adjacent consonents
    List to store sorted adjacent consonents list
Algorithm:
    1) Count the number of adjacent consonents for each string in the input list
    2) Store number of adjacent consonents in a dictionary assigning the number to the input string as the key.
    3) Create a new list, appending strings based on highest number of adjacent consonents
    4) Return the new sorted list

    1:
    Input: string
    Output: Integer representing max number of adjacent consonents in string
    Set max number of adjacent consonents to 0
    Set consonents substring = ""
    For each character in the input string
        If the character is a consonent:
            Append the character to consonents substring
        Else the character is not a consonent:
            If length of consonents substring is >= 2:
                Set max number of adjacent consonents to length of consonents
            Set consonents substring to an empty string
    Return max number of adjacent consonents

   3:
   Set max number = Dictionary[0]
   Iterate through Dictionary
   If current value in Dictionary > max number, Set  = current value


   Store whichever came first, first in the sorted list 
"""

VOWELS = ["a", "e", "i", "o", "u"]


def sort_by_consonant_count(list_of_strings):
    list_of_strings.sort(key=calculate_adjacent_consonants, reverse=True)
    return list_of_strings


def calculate_adjacent_consonants(input_string: str) -> int:
    max_number_of_adjacent_consonants = 0
    consonants_substring = ""
    cleaned_string = input_string.strip().lower()

    for letter in cleaned_string:
        if letter in VOWELS:
            if len(consonants_substring) >= 2:
                max_number_of_adjacent_consonants = len(consonants_substring)
            consonants_substring = ""
        else:
            consonants_substring += letter

    if len(consonants_substring) > max_number_of_adjacent_consonants:
        max_number_of_adjacent_consonants = len(consonants_substring)
    return max_number_of_adjacent_consonants


my_list = ["aa", "baa", "ccaa", "dddaa"]
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ["can can", "toucan", "batman", "salt pan"]
print(sort_by_consonant_count(my_list))
# ["salt pan", "can can", "batman", "toucan"]

my_list = ["bar", "car", "far", "jar"]
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ["day", "week", "month", "year"]
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ["xxxa", "xxxx", "xxxb"]
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
