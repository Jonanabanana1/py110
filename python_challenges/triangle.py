# Write a program to determine whether a triangle is equilateral, isosceles, or scalene.

# An equilateral triangle has all three sides the same length.

# An isosceles triangle has exactly two sides of the same length.

# A scalene triangle has all sides of different lengths.

# Note: For a shape to be a triangle at all, all sides must be of length > 0, and the sum of the lengths of any two sides must be greater than the length of the third side.

"""
P:
Determine whether a triangle is equilateral, isosceles, or scalene

Equilateral: All sides are the same length
Isosceles: Exactly 2 sides are the same length
Scalene: All sides are different length

Requirements:
    - All sides must have length > 0
    - Smallest 2 sides must add up to be greater than largest side
    - No negative side length

Examples:
    10, 10, 10 = Equilateral
    1, 2, 5 = Not a triangle because 1 + 2 < 5
    10, 10, 11 = Isosceles
    10, 11, 12 = Scalene

Data Structures:
    list to hold the side lengths

Algorithm:
    1) Sort the sides based on length from lowest to highest
        -sorted/sort
    2) Check if the two lowest add up to be greater than highest
        - If not return Not a triangle
    3) Check if first 2 elements are the same
        Yes: Check if second element is equal to the third element in the list
            If yes, Equilateral
            If no, Isosceles
        No: Scalene

"""


class Triangle:
    def __init__(self, side_a, side_b, side_c) -> None:
        side_a, side_b, side_c = sorted((side_a, side_b, side_c))
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        for side in (side_a, side_b, side_c):
            if side <= 0:
                raise ValueError(
                    f"Invalid side length {side}. Side must be greater than 0"
                )

        if side_a + side_b <= side_c:
            raise ValueError(
                "Smallest 2 sides must add up to be greater than third side"
            )

    @property
    def kind(self):
        if self.side_a == self.side_b:
            if self.side_b == self.side_c:
                return "equilateral"
            return "isosceles"
        elif self.side_b == self.side_c:
            return "isosceles"
        return "scalene"
