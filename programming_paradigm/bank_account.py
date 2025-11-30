# programming_paradigm/bank_account.py

def safe_divide(numerator, denominator):
    """
    Safely divide numerator by denominator.

    Returns:
    - "Error: Please enter numeric values only." for non-numeric inputs
    - "Error: Cannot divide by zero." for denominator == 0
    - "The result of the division is X" for successful division
    """
    # Validate numeric conversion
    try:
        num = float(numerator)
        den = float(denominator)
    except (ValueError, TypeError):
        return "Error: Please enter numeric values only."

    # Division, with explicit handling of division by zero
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    # Return formatted result (keeps float representation)
    return f"The result of the division is {result}"
