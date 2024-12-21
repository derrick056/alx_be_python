number = int(input("Enter a number to see its multiplication table:"))

y = 1
for y in range(10):
    y +=1
    z = number * y
    print(f"{number} * {y} =", z)