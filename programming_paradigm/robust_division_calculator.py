def safe_divide(numerator: float, denominator:float):
    try:
        result= numerator/ denominator
        return f"The result of the division is {result:.2f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
    
