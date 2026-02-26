def add(a,b):
    return a + b
def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
    
def main():
    print("=== Simple Calculator ===")
    print("Type 'exit' to quit anytime.")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        else:
            print("Operations: +  -  *  /")
            operation = input("Choose operation: ")
                
            if operation == "+":
                result = add(num1, num2)
            elif operation == "-":
                result = subtract(num1, num2)
            elif operation == "*":
                result = multiply(num1, num2)
            elif operation == "/":
                result = divide(num1, num2)
            else:
                result = "Invalid operation selected"
            
            print(f"Result: {result}")

            again = input("\nCalculate again? (yes/quit): ")
            if again.lower() == "quit":
                print("Goodbye!")
                break
main()