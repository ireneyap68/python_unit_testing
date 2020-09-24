def add(x, y):
    """Add Function"""

    return x + y

def subtract(x, y):
    """Subtract Function"""

    return x - y

def multiply(x, y):

    return x * y

def divide(x, y):

    if y == 0:
        return ValueError('you cannot put 0')
    return x / y