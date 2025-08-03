import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='calculator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_operation(op_str):
    logging.info(op_str)

def calculate(a, b, operator):
    try:
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a / b
        elif operator == '**':
            result = a ** b
        elif operator == '//':
            result = a // b
        elif operator == '%':
            result = a % b
        else:
            raise ValueError("Unsupported operator.")
        log_operation(f"{a} {operator} {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero attempted.")
        return "❌ Error: Division by zero."
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return f"❌ Error: {str(e)}"

def main():
    print("🧮 Welcome to Custom CLI Calculator (type 'exit' to quit)")
    while True:
        try:
            user_input = input("\nEnter operation (e.g. 3 + 2): ").strip()
            if user_input.lower() == 'exit':
                print("👋 Goodbye!")
                break
            parts = user_input.split()
            if len(parts) != 3:
                print("❗ Format must be: number operator number (e.g. 5 * 6)")
                continue

            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])

            result = calculate(a, b, operator)
            print(f"✅ Result: {result}")
        except ValueError:
            print("❗ Invalid input. Please enter numbers properly.")

if __name__ == "__main__":
    main()
