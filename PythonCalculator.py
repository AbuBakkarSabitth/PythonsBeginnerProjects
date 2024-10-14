# Python calculator

# Take operator and numbers as input
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# Perform the calculation based on the operator
if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
        print(round(result, 3))
    else:
        print("Error: Division by zero is undefined.")
else:
    print("Invalid operator.")
