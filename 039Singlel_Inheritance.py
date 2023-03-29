class Employee:
    no_of_leaves = 4

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary}. Role is {self.role}"

class Programmer(Employee):
    no_of_holidays = 56
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = languages

    def printprog(self):  # This will return string not print String
        return f"The Programmer's Name is {self.name}. Salary is {self.salary}. Role is {self.role}. Languages are {self.language}"

harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 399, "Student")

Shubham = Programmer("Shubham", 333, "Programmer", ["Python"])
karan = Programmer("Karan", 888, "Programmer", ["Python", "cpp"])

print(karan.no_of_holidays)
Shubham.printprog()

print(Shubham.printprog())