def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# Taking input
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
except ValueError:
    print("Please Enter a valid number")
    exit(1)

Operator = input("Enter the operator: ")

if Operator == '+':
            print(num1, "+", num2, "=", add(num1, num2))

elif Operator == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

elif Operator == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

elif Operator == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Please enter a operator from + , - , * , / ")