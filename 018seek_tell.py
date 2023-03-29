f = open("99999sample.txt")
print(f.tell()) # shows where is the pointer
print(f.readline())
print("This line will not read as pointer is at end", f.readline())
print("now the pointer will be at 5", f.seek(5))
print(f.readline())

f.close()
