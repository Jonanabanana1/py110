"""

P:
    I stands for 1
    V stands for 5
    X stands for 10
    L stands for 50
    C stands for 100
    D stands for 500
    M stands for 1,000
    We don't have to worry about numbers higher than 3,000.

    1: I
    2: II
    3: III
    4: IV
    5: V
    6: VI
    7: VII
    8: VIII
    9: IX
    10: X

    1990
    1000=M
    900=CM
    90=XC

    Write some code that converts modern decimal numbers into their Roman number equivalents.

    Requirements:
        Make a RomanNumeral Class that creates a roman numeral object that accepts an integer as an argument. The class should have a to_roman() instance method to convert the number to its roman equivalent. The return value is a string

    Algorithm:
    1) Break number down by place value
        1987
        1000s = 1000 * 1
        900 = 900 * 1
        80 = 80 * 1
        7 = 7 * 1
    2) Match each place value to roman numerals
        1000 = M
        900 = CM
        80 = LXXX
        7 = VII
    3) Put it together
        MCMLXXXVII

    Determining place value:
    number = 5012
    while number / 10 != 0 (Number is greater than or equal to 10)
        number % 10 = current digit 2
        Determine the roman numeral for 2 based on I,V,X
        Store roman numeral
    Next iteration
        number % 10 = current digit 1
        Determine the roman numeral for 1 based on X, L, C
        Store roman numeral
    Next iteration
        number % 10 = 0
        Skip
        If wasnt 0, determine based on C, D, M
    Next iteration number % 10 = 5
        Determine roman numeral for 5 based on C, D, M
    At the end of eatch iteration remember to do number /= 10 to decrease the number digits

    How to determine what digit corresponds to what roman numeral.
    Have 3 tuples consisting of 3 roman numerals corresponding to the place values
    ones: (I, V, X)
    tens: (X, L, C)
    Hundreds/Thousands: (C, D, M)

    Select the corresponding tuple depending on which iteration you are on, first iteration utilizes ones, second uses tens, third+ uses hundreds/thousands

    If the number is 1-3, Roman numeral is just the first element of the tuple * digit. EX: 2 = I * 2 == II

    If number is 40, Roman numeral is first element plus second element EX: 4 = X + L (If on second interation) == XL

    If number is 5, roman numeral is second element of tuple

    6-8 is second element plus first element * (number-5)
    Ex: 700 = D + C*(7-5) = DCC

    9 is first element plus third element

    0/10 go to next digit and use the 3rd element of that tuple that number of digit times


"""


class RomanNumeral:
    numeral_tuples = (("I", "V", "X"), ("X", "L", "C"), ("C", "D", "M"))

    def __init__(self, num) -> None:
        if num <= 0:
            raise ValueError("Roman numerals must have value greater than 0")
        self.num = num

    def to_roman(self):
        total_numeral = ""
        current_place_value = 0
        decreasing_num = self.num

        while True:
            current_digit = decreasing_num % 10

            if current_place_value > 2:
                numeral = third_element * current_digit
                total_numeral = numeral + total_numeral
                break

            first_element = RomanNumeral.numeral_tuples[current_place_value][0]
            second_element = RomanNumeral.numeral_tuples[current_place_value][
                1
            ]
            third_element = RomanNumeral.numeral_tuples[current_place_value][2]

            match current_digit:
                case 1 | 2 | 3:
                    numeral = first_element * current_digit
                case 4:
                    numeral = first_element + second_element
                case 5:
                    numeral = second_element
                case 6 | 7 | 8:
                    numeral = second_element + first_element * (
                        current_digit - 5
                    )
                case 9:
                    numeral = first_element + third_element
                case 0:
                    numeral = ""

            current_place_value += 1
            total_numeral = numeral + total_numeral
            decreasing_num //= 10
            if decreasing_num == 0:
                break

        return total_numeral
