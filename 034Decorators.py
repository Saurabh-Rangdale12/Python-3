def fun1(num):
    if num == 0:
        return print
    if num == 1:
        return sum

a = fun1(1)
print(a)

def executor(func):
    func("This")

executor(print)

def dec1(func2):
    def nowexec():
        print("Executing now")
        func2()
        print("Executed")
    return nowexec()

# def who():
#     print("Saurabh")

@dec1
def who():
    print("Saurabh")

# who = dec1(who)  # this is decorating it means who will became nowexec function

who
