n = int(input("Enter no. of Rows: "))
i = 1
k = n
while(k):
    j = i
    while(j):
        print("*", end="")
        j = j-1
    k = k -1
    i = i+1
    print("")