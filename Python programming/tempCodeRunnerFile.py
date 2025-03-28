def fibonacci(n):
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)