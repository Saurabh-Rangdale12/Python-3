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

    @classmethod
    def from_str(cls, string):
        # param = string.split("-")  # param will be list
        # return cls(param[0], param[1], param[2])

        return cls(*string.split("-"))  # *-> any no. of arguments


harry = Employee("Harry", 3444, "instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_str("karan-490-Student")

print(karan.role)

