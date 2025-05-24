import os

os.system("clear")
# print("Current Working Directory:", os.getcwd())
# file = open("example.txt", "r")
# for line in file:
#     print(repr(line))
# file.close()
file = open("output.txt", "a")
# file.write("Hello world!\n")
# lines = ["First line\n", "Second line\n"]
# file.writelines(lines)
file.write("Third line\n")
file.write("Last line\n")
file.close()
