with open("99999sample.txt") as f:
    a = f.read(4)
    print(a)
    # f.seek(0)
    a = f.readlines()
    print(a)
    f.close()

f = open("99999sample.txt")
f.readlines()