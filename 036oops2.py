class Employee:
    no_of_leaves = 0
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = "455"
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = "677"
rohan.role = "Student"

print(rohan.__dict__)
print(harry.__dict__)

print(harry.salary, rohan.role, harry.no_of_leaves)
print(Employee.no_of_leaves)

rohan.no_of_leaves = 9  # it will not change no of leaves value in employee class
print(rohan.__dict__)
Employee.no_of_leaves = 10  # it will change it
print(Employee.__dict__)

print(harry.no_of_leaves)
