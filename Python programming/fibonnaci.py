def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    :param n: The position in the Fibonacci sequence (0-indexed).
    :return: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



# Example usage
if __name__ == "__main__":
    n = 8  # Change this value to compute a different Fibonacci number
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")