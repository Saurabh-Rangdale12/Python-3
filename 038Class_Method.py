class Employee:
    no_of_leaves = 0

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def pirntdetails(self):  # it is function in class
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod  # it is decorator built in
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves  # change no_of_leaves to new leaves of class not object


harry = Employee("Harry", 3444, "insturctor")
rohan = Employee("Rohan", 455, "Student")

# print(rohan.no_of_leaves)

rohan.change_leaves(22)  # it changes no of leaves frm the class

print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)
