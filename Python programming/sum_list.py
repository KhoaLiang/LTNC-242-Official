def sum_list(numbers):
    if not numbers:  # Base case: empty list
        return 0
    # Recursive case: sum the first element with the sum of the rest
    return numbers[0] + sum_list(numbers[1:])

# Example usage:
print(sum_list([1, 2, 3]))        # Output: 6
print(sum_list([1, 2, 0, 3]))     # Output: 6
print(sum_list([1, 2, 0, -3]))    # Output: 0