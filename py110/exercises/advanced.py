import pdb
import os
os.system('clear')

'''
Problem: Given a 3x3 matrix, return the transpose of that matrix. The transpose of the matrix is where the columns and rows are switched.
Example:
    Input: [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9], 
    ]
    Output: [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9], 
    ]

Input: 3x3 2d list that contains integers as elements
Output: Transpose of the list 

Requirements:
    - Can not modify/mutate the input list
    - Each inner list in the transpose represents the column in the input

Ideas:
    zip() to pair elements together

Algorithm:
    - Grab a column in the input matrix
        * Use zip() to get tuple with first 3 elements in each list paired
        * Grab each tuple in zip and convert it to a list to add to output
    - Add that column to the output matrix
    - Repeat that for each inner list

'''

# def transpose(matrix: list):
#     transposed_matrix = zip(*matrix)
#     return [list(nested_list) for nested_list in transposed_matrix]
# matrix = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]

# new_matrix = transpose(matrix)
# print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
# print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True

# # Now do it except make it work for any number of rows and columns
# # All of these examples should print True
# print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
# print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
# print(transpose([[1]]) == [[1]])

# matrix_3_by_5 = [
#     [1, 2, 3, 4, 5],
#     [4, 3, 2, 1, 0],
#     [3, 7, 8, 6, 2],
# ]
# expected_result = [
#     [1, 4, 3],
#     [2, 3, 7],
#     [3, 2, 8],
#     [4, 1, 6],
#     [5, 0, 2],
# ]
# print(transpose(matrix_3_by_5) == expected_result)

'''
Given a matrix of any size MxN, return a 90 degree rotated matrix. The
rotated matrix must be a new matrix and the original matrix must not be
mutated.

Ex:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Output:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

Ideas:
    Each nested list in the output is the same as a column in the input list but reversed
    I can use the transpose function, but at the end reverse the list.
'''
# def rotate90(matrix):
#     transposed_matrix = transpose(matrix)
#     for idx in range(len(transposed_matrix)):
#         transposed_matrix[idx].reverse()
#     return transposed_matrix
# matrix1 = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]

# matrix2 = [
#     [3, 7, 4, 2],
#     [5, 1, 0, 8],
# ]

# new_matrix1 = rotate90(matrix1)
# new_matrix2 = rotate90(matrix2)
# new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# # These examples should all print True
# print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
# print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
# print(new_matrix3 == matrix2)


# Write a function that takes two sorted lists as arguments and returns a new list that contains all the elements from both input lists in ascending sorted order. You may assume that the lists contain either all integer values or all string values.
# You may not provide any solution that requires you to sort the result list. You must build the result list one element at a time in the proper order.
# Your solution should not mutate the input lists.
'''
Input: two sorted lists
Output: new list containing all elements in input in ascending order

Requirements:
    - Lists contain all integer or all string values
    - You can not sort the result list
    - Must build result list one element at a time in the right order
    - Can not mutate input lists
    - If a list is empty, return the other list

Ideas:
    - Create a variable that points to each element in the two lists
    - Compare the element in one list to the other
    - Add the one that's less to the result list and increment the designated pointer
    - If the two elements are equal, always add the left element
    - Compare again with the pointers
Algorithm:
    - Create two variables, list_1_pointer and list_2_pointer
    - Initialize the result list
    - Set the two pointers to point to the first element in each list
    - Compare the values and add the smallest value to the result
    - If the values are equal, add list_1's value to the result
    - Increment whichever's list pointer that got its element added
    - Repeat steps 4-6 until one of the pointers is equal to the length of their designated list
    - At that point, add the rest of the elements of the other list and break out of the loop
    - Return the final resulting list
'''
def merge(lst1: list, lst2: list):
    if not lst1:
        return lst2
    if not lst2:
        return lst1

    lst_1_pointer = 0
    lst_2_pointer = 0
    result_list = []

    while True:
        if lst1[lst_1_pointer] <= lst2[lst_2_pointer]:
            result_list.append(lst1[lst_1_pointer])
            lst_1_pointer += 1
        else:
            result_list.append(lst2[lst_2_pointer])
            lst_2_pointer += 1
        if lst_1_pointer == len(lst1):
            result_list.extend(lst2[lst_2_pointer:])
            break
        if lst_2_pointer == len(lst2):
            result_list.extend(lst1[lst_1_pointer:])
            break
    return result_list

# All of these examples should print True
# print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
# print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
# print(merge([], [1, 4, 5]) == [1, 4, 5])
# print(merge([1, 4, 5], []) == [1, 4, 5])

# names1 = ['Alice', 'Kim', 'Pete', 'Sue']
# names2 = ['Bonnie', 'Rachel', 'Tyler']
# names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
#                   'Rachel', 'Sue', 'Tyler']
# print(merge(names1, names2) == names_expected)

'''
Input: Unsorted list of either integers or strings
Output: Sorted list 

Requirements:
    - Must sort using merge sort algorithm
    - Can use merge function
Merge-sort Algorithm:
    1) Partition list into two lists each with half the elements
    2) Keep partioning list splitting it into halves until you get a list containing only 1 element
    3) Merge the 1 element list with another 1 element list
    4) Keep doing that until you get back to an original sorted list
Ideas:
    Grab the length of current list
    Divide the length by 2 to get index at which to split the list
    Subtract by 1 to account for zero index unless the end parameter is exclusive. Anyways the actual index should be subtracted by 1
    Repeat that process through recursion calling the same function but this time with the split list
    We want to return when the length of the list is 1
    When we return the list of length 1 back up, the upper function should use merge() to merge the list with another bottom list
    The output of that merge should be used by the upper upper function
    
Algorithm:
    1) Grab the length of input list
    2) If the length of the input list is 1, return the input list
    3) Initialize middle_index to length of list / 2
    4) Split the input list into two lists, lst1 and lst2
    5) Invoke merge(merge_sort(lst1), merge_sort(lst2)) with the two lists being the ones we get from splitting
    6) return the final result of the merge() 
'''
def merge_sort(input_list):
    list_length = len(input_list)
    if list_length == 1:
        return input_list

    middle_index = list_length // 2
    left_lst = input_list[0:middle_index]
    right_lst = input_list[middle_index:]

    return merge(merge_sort(left_lst), merge_sort(right_lst))
# All of these examples should print True
# print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
# print(merge_sort([5, 3]) == [3, 5])
# print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
# print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

# original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#             'Kim', 'Bonnie']
# expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
#             'Sue', 'Tyler']
# print(merge_sort(original) == expected)

# original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
#             43, 5, 25, 35, 18, 46]
# expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
#             35, 37, 43, 46, 51, 54]
# print(merge_sort(original) == expected)

'''
Input: sorted list of numbers or strings and the element in the list to search
Output: Integer representing the index of the element in the list

Requirements:
    - If the element is not in the list, return -1
    - Input will always be sorted
    - Must use a binary search algorithm to find element

Get index for 9
    [1, 2, 3, 4, 5, 6, 7, 8, 9] -> start:5, 5 + 3 = 8 
    [6, 7, 8, 9] -> start: 2, 2 + 1 = 3
    [8, 9] -> Returns 1


Binary search:
    - Base Case:
    - If length of list is 1: Check if element is in the list and return the index at which it appears in the mini list
    
    - Function:
    - Initialize a middle index by taking length // 2
    - Compare value at middle index with element
    - If equal, return middle index
    - If greater, invoke Function passing in greater half of list
    - If lesser, invoke Function passing in lesser half of list
    - Store starting index in which you start the next list
    - Return the value of starting index + returned value from bottom
    - If returned value from bottom is -1, return -1
    
'''
def binary_search(lst: list, element):
    lst_length = len(lst)
    if lst_length == 1:
        if lst[0] != element:
            print('x')
            return -1

    middle_index = lst_length // 2
    middle_value = lst[middle_index]
    
    if element == middle_value:
        return middle_index
    if element > middle_value:
        start_index = middle_index  
        lower_index = binary_search(lst[middle_index:], element)
        if lower_index == -1:
            return -1
        return start_index + lower_index
    else:
        lower_index = binary_search(lst[:middle_index], element)
        if lower_index == -1:
            return -1
        return lower_index
# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)