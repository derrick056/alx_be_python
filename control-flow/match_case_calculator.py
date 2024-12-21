no1 = int(input("Enter the first number:"))
operation = input("Choose the operation (+, -, *, /):")
no2 = int(input("Enter the second number:"))

match operation:
    case "+":
        print(f"{no1} {operation} {no2} =", no1 + no2)
    
    case "-":
        print(f"{no1} {operation} {no2} =", no1 - no2)

    case "*":
        print(f"{no1} {operation} {no2} =", no1 * no2)
    
    case "/":
        print(f"{no1} {operation} {no2} =", no1 / no2)

    