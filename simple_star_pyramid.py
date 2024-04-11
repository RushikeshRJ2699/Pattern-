rows = int(input("Enter Row Number "))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if j <= i:
            print("*",end=" ")
    print(" ")