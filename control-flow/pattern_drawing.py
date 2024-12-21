x = int(input("Enter the size of the pattern:"))
y=0
while y <= x:
    for z in range(x):
        print("*", end="")

    print()
    y +=1