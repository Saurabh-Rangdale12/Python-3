print("Enter num1: ")
num1 = input()
print("Enter num2 : ")
num2 = input()

try:
    print("The sum of these two numbers is", # try this if not working then
          int(num1) + int(num2))
except Exception as kar: # this will execute and program will run below
    print(kar) # it print that above try code is not working
    print("except kar")

print("This line is very important.!!")