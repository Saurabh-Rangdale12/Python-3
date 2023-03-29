n = 34
print("You Have 5 Chance to guess a number")

i = 5

while(i>0):
    num = int(input("Enter Number: "))
    if num<34:
        print("Your number is lesser")
    elif num>34:
        print("Your number is Greater")
    else:
        print("You Have Correctly Guess the number in ", i, "Chances. Congradulation!!!")
        break
    i = i-1
    print("You Have ", i, "Chances Left")