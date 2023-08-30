num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

# List of available operators
available_operators = ["+", "-", "*", "/", "%"]

print("Available operators:")
for op in available_operators:
    print(op)

operator = input("Please choose the desired operator: ")

if operator in available_operators:
    if operator == "+":
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"The subtraction of {num2} from {num1} is {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"The multiplication of {num1} and {num2} is {result}")
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The division of {num1} by {num2} is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    elif operator == "%":
        result = num1 % num2
        print(f"The modulo of {num1} by {num2} is {result}")
else:
    print("Invalid operator. Please choose a valid operator from the list.")
