print("operator to use")
op = input()
print("numbers for operating")
num1 = int(input())
num2 = int(input())

if num1 == 45 and num2 == 3 and op == '*':
    print(num1, op, num2, " = ", 555)
elif num1 == 56 and num2 == 9 and op == '+':
    print(num1, op, num2, " = ", 77)
elif num1 == 56 and num2 == 6 and op == '/':
    print(num1, op, num2, " = ", 4)
elif op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
else:
    print(num1 / num2)