from langchain.tools import tool
@tool
def calculator(a: int, b: int, operation: str) -> int:
    """Calculate the result of a mathematical operation
    
    Args:
        a: The first number
        b: The second number
        operation: The operation to perform (add, subtract, multiply, divide, percentage)
    Returns:
        The result of the operation
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    elif operation == "percentage":
        return a * b / 100
    else:
        return "Invalid operation"