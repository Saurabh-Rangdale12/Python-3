class Dad:
    basketball = 5

class Son(Dad):
    dance = 2
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance = 7
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!\nYes I dance very awesomely {self.dance} no of times"


darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())
# k = harry.basetball
print(harry.basketball)