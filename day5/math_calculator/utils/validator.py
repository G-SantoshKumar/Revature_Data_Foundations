import re

def is_valid_expression(expression: str) -> bool:
    pattern = r'^[0-9+\-*/()\s]+$'
    return bool(re.match(pattern, expression))

