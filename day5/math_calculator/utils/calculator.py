import math




def calculate(expression: str) -> float:
    try:
        result = eval(expression, {"__builtins__": {}},{"math":math})
        return float(result)
    
    except ZeroDivisionError:
        raise ValueError("Error: Division by zero is not allowed.")
    except Exception:
        raise ValueError("Error: Invalid mathematical expression.")

 


