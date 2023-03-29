class Student:
    pass  # pass if we not want any thing in class or function

harry = Student()  # it is an object
larry = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["hindi", "physics"]

print(harry.name, larry.subjects)