#  “Diamond Shape Problem.”. It is about priority related confusion,
#  which arises when four classes are related to each other by an inheritance relationship,
#  as shown in the image below:

class A:
    def met(self):
        print("Class A")


class B(A):
    def met(self):
        print("Class B")


class C(A):
    def met(self):
        print("Class C")


class D(C, B):  # if fuction is not in this class then it will search 1st in class C
    pass
    # def met(self):
    #     print("Class D")


a = A()
b = B()
c = C()
d = D()

d.met()