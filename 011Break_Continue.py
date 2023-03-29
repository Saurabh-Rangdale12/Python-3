# i = 0
# while(True):
#     if i<=5:
#         i = i+1
#         continue # niche ka sab kuch bhool jao aur continue karo firse
#     print(i)
#     if(i == 44):
#         break #stop the loop
#     i = i+1

while(True):
    num = int(input("Enter a Number: "))
    if num > 100:
        print("Entered number is greater than 100\n")
        break
    else:
        print("Try again!\n")
        continue 