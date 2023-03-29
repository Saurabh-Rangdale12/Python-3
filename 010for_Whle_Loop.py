# list = ["Harry", "Larry", "Carry", "Marie"]
#
# for item in list:
#     print(item)

# list1 = [["Harry", 1], ["Larry", 2], ["Carry", 3], ["Marie", 6]]
#
# dict1 = dict(list1) # convertin list1 to dictionary!!!
# print(dict1)

# for item, lollypop in list1:
#     print(item, "and chocolate is ", lollypop)

# for item in dict1:
#     print(item)

items = [int, float, "Harry", 5,3,4,2,44,5,6,22,3,4,7,6]

for item in items:
    if str(item).isnumeric() and item >= 6:
        print(item)

i = 0
while(i<45):
    print(i)
    i = i+1