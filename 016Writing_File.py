# f = open("99999sample.txt", "w") # "a" - append for writing at end of existin file
# a = f.write("Saurabh is my name") # "w" - it erase the content of file and write new conten always
# print(a)
# f.close()

# Handle xread and write both
f = open("99999sample.txt", "r+")
print(f.read())
f.write("\nThank you")