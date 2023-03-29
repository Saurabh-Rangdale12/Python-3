class Employee:
    no_of_leaves = 4
    var = 99

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary}. Role is {self.role}"


class Player:
    var = 8
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

class CoolProgrammer(Player, Employee):
    languages = "C++"
    def printlanguage(self):
        print(self.languages)


harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 399, "Student")

shubham = Player("Shubham", ["Cricket"])
karan = CoolProgrammer("Karan", ["Foot Ball"])
# karan = CoolProgrammer("karan", 566, "coolprogrammer")  # this will give error because we put player first and then employee

print(karan.var)
karan.printlanguage()
print(karan.printdetails())
