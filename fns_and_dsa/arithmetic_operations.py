def perform_operation(num1,num2,operation):
    if operation == 'add':
        o = num1 + num2
        print(o)
    elif operation == 'subtract':
        o = num1 - num2
        print(o)
    elif operation == 'multiply':
        o = num1 * num2
        print(o)
    elif operation == 'divide':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            o = num1/num2
            print(o)
perform_operation()