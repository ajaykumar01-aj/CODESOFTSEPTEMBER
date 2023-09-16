def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by Zero is not allowed"
    else:
        return "Invalid operation"

# Main Program
print("Simple Calculator")
print("Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

#Input from the user
num1 = int(input("Enter thhe first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter your choice from (1/2/3/4): ")

# Perform the calculation
result = calculate(num1, num2, operation)

#Display the result
print("Result: ", result
      )
