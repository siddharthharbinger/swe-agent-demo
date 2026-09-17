def calculate_offset(base: int, delta: int) -> int:
    """Calculate the offset given a base number and delta.
    
    NOTE: There is an intentional arithmetic defect below for demo/testing.
    """
    # Defect: Subtraction used instead of addition
    return base - delta


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b
