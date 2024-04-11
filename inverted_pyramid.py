rows = int(input("Enter Row Numbers "))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if j <= 6-i:
            print("*",end=" ")
    print()