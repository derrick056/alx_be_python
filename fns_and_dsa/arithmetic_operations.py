def perform_operation(num1, num2, operation):
    try:
        if operation== 'add':
           return num1 + num2
    
        elif operation== 'subtract':
           return num1 - num2
    
        elif operation== 'multiply':
           return num1 * num2
    
        elif operation== 'divide':
           return num1 / num2
    
        elif operation== 'divide':
           return num1 / num2
    
        elif num1 or num2/0:
           return "error"
   
        else:
          return "invalid operation"
        
    
    except ZeroDivisionError:
       return "invalid division by 0"