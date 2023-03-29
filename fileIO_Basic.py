# File IO Basics
"""
"r" - open file for reading
"w" - open a file for writing
"x" - creates file if not exits
"a" - Add more content to a file
"t" - text mode
"b" - binary mode
"+" - read and write
"""

f = open("99999sample.txt", "rt")
# print(f.readlines())
# print(f.readlines())
# print(f.readlines())
# print(f.readlines())

# content = f.read()
# print(content)

# for line in f:
#     print(line, end="")

content = f.read(34466)
print("1", content)

content = f.read(55667)
print("2", content)
f.close # it is most imp function

# Above is type to read file