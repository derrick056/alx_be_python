number = int(input("Enter a number to see its multiplication table:"))

y = 0
for y in range(1,11):
    y +=1
    z = number * y
    print(f"{number} * {y} =", z)