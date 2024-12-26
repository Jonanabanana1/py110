import os

os.system("clear")
# Write a function that takes a string and returns a dictionary containing the following three properties:
# the percentage of characters in the string that are lowercase letters
# the percentage of characters that are uppercase letters
# the percentage of characters that are neither
# All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. Each value should be rounded to two decimal points.
# You may assume that the string will always contain at least one character.
# '''
# Input: string
# Output: Dictionary containing three keys that show percentage properties
# Requirements:
#     - Output dictionary keys are 'lowercase', 'uppercase', 'neither'
#     - Output dict values are in string represent percentages between 0 - 100
#     - Output values should be rounded to 2 decimal places
#     - String will always contain 1 character
#     - Any character that is not alphabetic is considered neither
# Algorithm:
#     - Iterate through the string
#     - Check if the character is lowercase, uppercase, or neither
#     - Increment a counter variable for the specific case
#     - At the end find the percentage by dividing counter to length of string
# '''
# def letter_percentages(string: str):
#     lower_counter = 0
#     upper_counter = 0
#     neither_counter = 0
#     for char in string:
#         if not char.isalpha():
#             neither_counter += 1
#             continue
#         if char.isupper():
#             upper_counter += 1
#             continue
#         lower_counter += 1
#     result = {}
#     result['lowercase'] = f'{(lower_counter / len(string) * 100):.2f}'
#     result['uppercase'] = f'{(upper_counter / len(string) * 100):.2f}'
#     result['neither'] = f'{(neither_counter / len(string) * 100):.2f}'
#     return result

# expected_result = {
#     'lowercase': "50.00",
#     'uppercase': "10.00",
#     'neither': "40.00",
# }
# print(letter_percentages('abCdef 123'))
# print(letter_percentages('abCdef 123') == expected_result)

# expected_result = {
#     'lowercase': "37.50",
#     'uppercase': "37.50",
#     'neither': "25.00",
# }
# print(letter_percentages('AbCd +Ef') == expected_result)

# expected_result = {
#     'lowercase': "0.00",
#     'uppercase': "0.00",
#     'neither': "100.00",
# }
# print(letter_percentages('123') == expected_result)

# A triangle is classified as follows:
# Equilateral: All three sides have the same length.
# Isosceles: Two sides have the same length, while the third is different.
# Scalene: All three sides have different lengths.

# To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side, and every side must have a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

# Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.

"""
Input: 3 float values representing lengths of a side in a triangle
Output: String representing type of trangle or invalid
Requirements:
    Valid Triangle:
        - Sum of two shortest sides is greater than longest side
        - Sides must have length greater than 0
    Equilateral - All sides have the same length
    Isosceles - 2 sides have the same length
    Scalene - All sides are different length
Algorithm:
    Return invalid if any side is zero
    Determine two shortest sides
    Add two shortest side and compare with longest side
    Return invalid if sum of two shortest side is less than longest side
    Check side a and b are equal
    Check side b and c are equal
    Determine type of triangle
"""


# def triangle(side_a, side_b, side_c):
#     sides = [side_a, side_b, side_c]
#     if side_a <= 0:
#         return "invalid"
#     if side_b <= 0:
#         return "invalid"
#     if side_c <= 0:
#         return "invalid"

#     greatest_side = max(sides)
#     sides.remove(greatest_side)

#     if sum(sides) < greatest_side:
#         return "invalid"
#     if side_a == side_b == side_c:
#         return "equilateral"
#     if side_a == side_b or side_b == side_c or side_a == side_c:
#         return "isosceles"
#     return "scalene"


# print(triangle(3, 3, 3) == "equilateral")  # True
# print(triangle(3, 3, 1.5) == "isosceles")  # True
# print(triangle(3, 4, 5) == "scalene")      # True
# print(triangle(0, 3, 3) == "invalid")      # True
# print(triangle(3, 1, 1) == "invalid")      # True

# Write a triangle function that accepts angles as parameters and returns whether or not the triangle is an acute, right, or obtuse triangle
# Right: One angle is a right angle (exactly 90 degrees).
# Acute: All three angles are less than 90 degrees.
# Obtuse: One angle is greater than 90 degrees.
# Invalid: sum of three angles are not equal to 180


def triangle(angle1: int, angle2: int, angle3: int) -> str:
    angles = (angle1, angle2, angle3)
    if 0 in angles:
        return "invalid"
    if sum((angle1, angle2, angle3)) != 180:
        return "invalid"
    if 90 in angles:
        return "right"
    for angle in angles:
        if angle > 90:
            return "obtuse"
    return "acute"


# print(triangle(60, 70, 50) == "acute")  # True
# print(triangle(30, 90, 60) == "right")  # True
# print(triangle(120, 50, 10) == "obtuse")  # True
# print(triangle(0, 90, 90) == "invalid")  # True
# print(triangle(50, 50, 50) == "invalid")  # True
