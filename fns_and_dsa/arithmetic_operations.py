def perform_operation(num1,num2,operation):
    if operation == 'add':
        o = num1 + num2
        print(o)
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            return num1/num2
            print(o)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ")
result = perform_operation(num1, num2, operation)
print(f"Result: {result}")