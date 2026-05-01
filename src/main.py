"""
Command-line calculator with basic arithmetic operations.
Module 8 Assignment — Ostad AI/ML Bootcamp, Batch 6
Author: Farjana Ferdausi
"""

from utils import add, subtract, multiply, divide

def main():
    print("\n✨ Welcome to Farjana's Calculator ✨")
    print("Operations: +, -, *, /")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ").strip()
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("❌ Invalid operator. Please use +, -, * or /")
                continue

            print(f"✅ Result: {num1} {op} {num2} = {result}\n")


        except ValueError as e:
            print(f"❌ Error: {e}. Please try again.\n")


        except KeyboardInterrupt:
            print("\n👋 Calculator closed. Goodbye!")
            break

if __name__ == "__main__":
    main()