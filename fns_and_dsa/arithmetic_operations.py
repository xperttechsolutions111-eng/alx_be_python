def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations based on the operation parameter.

    Parameters:
    - num1 (float): first number
    - num2 (float): second number
    - operation (str): 'add', 'subtract', 'multiply', 'divide'

    Returns:
    - float: result of the arithmetic operation
    - str: error message in case of division by zero or invalid operation
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
