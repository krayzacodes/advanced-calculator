import math
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "❌ Cannot divide by zero!"
    return a / b
def power(a, b):
    return a ** b
def square_root(a):
    if a < 0:
        return "❌ Cannot take aquare root of negative number!"
    return math.sqrt(a)
def mod(a, b):
    return a % b


print("🧮 Advanced Calculator")
print("Select operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (x)")
print("4. Division (÷)")
print("5. Power (x^y)")
print("6. Square Root (√x)")
print("7. Modulus (%)")

choice =input("Enter choice (1-7): ")

if choice == '6':
    num = float(input("Enter number: "))
    print("Result:", square_root(num))
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", power(num1, num2))
    elif choice == '7':
        print("Result:", mod(num1, num2))
    else:
        print("❌ Invalid selection!")