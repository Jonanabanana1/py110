import os

os.system("clear")
# Name the method used to customize each of the following operators:
# Operator
# >     __gt__
# *     __mul__
# <=    __le__
# !=    __ne__
# +=    __iadd__
# **=   __ipow__
# //    __floordiv__

# Consider the following class:


class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() == other.name.casefold()

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() != other.name.casefold()

    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() < self.name.casefold()

    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() > self.name.casefold()

    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() <= self.name.casefold()

    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() >= self.name.casefold()


# tom = Cat("Tom")
# tom2 = Cat("tom")
# tommy = Cat("tommy")
# print(tom == tom2)
# print(tom2 == tommy)

# Create the methods needed so you can compare Cat objects for equality and inequality by their name value. The comparisons should ignore case and should work for the == and !=operators. If the right-hand operand is not a Cat object, the methods should return NotImplemented.

# Be sure to write test cases to demonstrate that your methods work as intended.

# Using the answer to the previous problem, create the methods needed so you can perform ordered comparisons of Cat objects by their name value. As with the previous problem, the comparison should ignore case. They should work for the <, <=, >, and >= operators. If the right-hand operand is not a Cat object, the methods should return NotImplemented.

# Be sure to write test cases to demonstrate that your methods work as intended.


# Consider the following class that represents 2D vectors:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Vector(self.x * other, self.y * other)


# print(Vector(3, 2) + Vector(5, 12))  # Vector(8, 14)
# print(Vector(5, 12) - Vector(3, 2))  # Vector(2, 10)
# print(Vector(5, 12) * 2)  # Vector(10, 24)
# print(3 * Vector(5, 12))  # Vector(15, 36)

# my_vector = Vector(5, 7)
# my_vector += Vector(3, 9)
# print(my_vector)  # Vector(8, 16)

# my_vector -= Vector(1, 7)
# print(my_vector)  # Vector(7, 9)

# print(Vector(3, 2) + 5)
# # TypeError: unsupported operand type(s) for +: 'Vector'
# # and 'int'


# Consider the following class that represents a value that can be either a string or an integer:
class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f"Silly({repr(self.value)})"

    def __add__(self, other):
        if type(self.value) is str and not self.value.isdigit():
            return Silly(f"{self.value}{other}")
        if type(other) is str and not other.isdigit():
            return Silly(f"{self.value}{other}")
        return Silly(int(self.value) + int(other))


print(Silly("abc") + "def")  # Silly('abcdef')
print(Silly("abc") + 123)  # Silly('abc123')
print(Silly(123) + "xyz")  # Silly('123xyz')
print(Silly("333") + 123)  # Silly(456)
print(Silly(123) + "222")  # Silly(345)
print(Silly(123) + 456)  # Silly(579)
print(Silly("123") + "456")  # Silly(579)
# Assuming we have an expression like Silly(x) + y, the evaluation rules are as follows:

#     If either x or y is a non-numeric string, concatenate the string values of x and y.
#     Otherwise, compute the sum of the integer values of x and y.

# Another way to word that is:

#     If both x and y can be expressed as integers, compute the sum of the integer values of x and y.
#     Otherwise, concatenate the string values of x and y.
