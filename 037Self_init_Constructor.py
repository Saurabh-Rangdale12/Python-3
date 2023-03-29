class Employee:
    no_of_leaves = 0

    def __init__(self, aname, asalary, arole):  # it is constructor
        self.name = aname
        self.salary = asalary
        self.role = arole

    def pirntdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

harry = Employee("Harry", 3444, "insturctor")
rohan = Employee("Rohan", 455, "Student")

# harry.name = "Harry"
# harry.salary = "455"
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = "677"
# rohan.role = "Student"

print(rohan.pirntdetails())
print(harry.pirntdetails())
