# Refactor the following program to use separate modules for each of the add_point and calculate_reflected_slope functions. You should also have a main program file that runs that last 4 lines of code shown below.

from file1 import calculate_reflected_slope
from file2 import add_point

add_point(4, 3)
add_point(1, -9)
slope = calculate_reflected_slope()
print(slope)  # Outputs: -4.0
