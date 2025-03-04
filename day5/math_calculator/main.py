import logging
from utils.validator import is_valid_expression
from utils.calculator import calculate

logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def main():
    print("Welcome to the Mathematical Expression Validator and Calculator!")
    while True:
        expression = input("Enter a mathematical expression (or 'exit' to quit): ")
        if expression.lower() == 'exit':
            logging.info("Exiting program.")
            print("Goodbye!")
            break

        if is_valid_expression(expression):
            logging.info(f"Valid expression: {expression}")
            result = calculate(expression)
            if result is not None:
                print(f"The result is: {result}")
                logging.info(f"Result of '{expression}' is {result}")
        else:
            print("Invalid expression! Please try again.")
            logging.warning(f"Invalid expression: {expression}")

if __name__ == "__main__":
    main()