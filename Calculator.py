num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

operations = {
    "+": num1 + num2,
    "-": num1 - num2,
    "*": num1 * num2,
    "/": num1 / num2 if num2 != 0 else "Error: Division by zero"
}

result = operations.get(operation, "Invalid operation")

print(f"{num1} {operation} {num2} = {result}" if isinstance(result, (int, float)) else result)

