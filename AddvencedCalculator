import os
import time
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Cannot divide by zero!"
def power(x, y):
    return x ** y
def modulus(x, y):
    return x % y

def menu():
    print("""
🧮 ADVANCED CALCULATOR MENU 🧮

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power (xⁿ)
6. Modulus (x mod y)
7. Clear screen
8. EXIT
---------------------
""")

while True:
    menu()
    choice = input("Select an operation (1-8): ")
    
    if choice == "8":
        print("Exiting... see you soon...")
        time.sleep(1)
        break
    elif choice == "7":
        clear_screen()
        continue
    elif choice in ["1", "2", "3", "4", "5", "6"]:
        try:
            x = float(input("Enter the firs number: "))
            y = float(input("Enter the second number: "))
        except ValueError:
            print("⚠️ Please enter a valid number!\n")
            continue
        if choice == "1":
            print("✅ Result:", add(x, y))
        elif choice == "2":
            print("✅ Result:", subtract(x, y))
        elif choice == "3":
            print("✅ Result:", multiply(x, y))
        elif choice == "4":
            print("✅ Result:", divide(x, y))
        elif choice == "5":
            print("✅ Result:", power(x, y))
        elif choice == "6":
            print("✅ Result:", modulus(x, y))

        input("\nPress Enter to continue...")  #pause
    else:
        print("⚠️ Invalid selection!\n")