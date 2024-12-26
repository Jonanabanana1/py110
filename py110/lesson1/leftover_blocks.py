"""
Problem:
Write a program that given a number of blocks, returns the amount of blocks left over after building the tallest valid possible structure.

Input:
  - Integer of total blocks
Output:
  - Integer of blocks left over after building tallest structure

Explicit rules:
  - Structure is built in layers
  - Top layer consist of 1 block
  - 1 block in an upper layer must be supported by 4 blocks in a lower layer
  - 1 block in a lower layer can support any amount of blocks in an upper layer
  - Each block must be connected

Implicit rules:
  - A block is any unit.
  - Total amount of blocks in each layer is equal to the layer number squared 

Questions:
  - Can there be half blocks?
  - Should the output be a string or integer?
  - What is the data type for the input?

Data Structure:
  - List representing total amount of blocks in each layer

Algorithm:
  1) Set current layer = 0
  2) Set current number of blocks = total number of blocks from input
  3) Calculate number of blocks needed to build current layer
  4) If current number of blocks < number of blocks needed to build current layer, return current number of blocks
  5) Else Set current number of blocks = current number of blocks - number of blocks needed to build current layer
  6) Increment current layer by 1
  7) Repeat steps 3-6
   
"""


def calculate_leftover_blocks(total_block_amount: int) -> int:
    current_layer = 0
    current_block_amount = total_block_amount

    while True:
        layer_block_amount = current_layer * current_layer

        if current_block_amount < layer_block_amount:
            return current_block_amount
        else:
            current_block_amount -= layer_block_amount

        current_layer += 1


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0)  # True
