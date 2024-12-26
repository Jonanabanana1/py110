# produce = {
#     "apple": "Fruit",
#     "carrot": "Vegetable",
#     "pear": "Fruit",
#     "broccoli": "Vegetable",
# }


# def select_fruit(items):
#     fruit_dictionary = {}

#     for item, category in items.items():
#         if category == "Fruit":
#             fruit_dictionary[item] = category

#     return fruit_dictionary


# print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }


def double_numbers(numbers, factor):
    doubled_numbers = []
    for number in numbers:
        doubled_numbers.append(number * factor)
    return doubled_numbers


my_numbers = [1, 4, 3, 7, 2, 6]
print(double_numbers(my_numbers, 3))  # [2, 8, 6, 14, 4, 12]
print(my_numbers)  # [1, 4, 3, 7, 2, 6]


# def double_odd_indexes(numbers):
#     doubled_numbers = []
#     for idx, number in enumerate(numbers):
#         if idx % 2 == 1:
#             doubled_numbers.append(number * 2)
#         else:
#             doubled_numbers.append(number)
#     return doubled_numbers


# my_numbers = [1, 4, 3, 7, 2, 6]
# print(double_odd_indexes(my_numbers))
