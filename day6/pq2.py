import logging

# Configure logging
logging.basicConfig(
    filename='./logs/app1.log',
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def divide_numbers(numbers, divisor):
    results = []
    for num in numbers:
        try:
            result = num / divisor
            results.append(result)
        except ZeroDivisionError:
            logging.error(f"Division by zero error for number: {num}")
            continue  
    return results

numbers_list = [10, 5, 0, 20, 0, 15]


divided_values = divide_numbers(numbers_list, 0)  

print("Valid results:", divided_values)
