# Public
# Protected
# Private


class Employee:
    no_of_leaves = 4
    var = 99

    _prct = 23
    __prv = 40

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary}. Role is {self.role}"

emp = Employee("harry", 677, "Programmer")
print(emp._prct)  # this will print protected var
# print(emp.__prv)  # this will give error as it is private
print(emp._Employee__prv)  # like this we access private var and function