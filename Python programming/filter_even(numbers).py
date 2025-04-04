def filter_even(numbers):
    return [num for num in numbers if num % 2 == 0]
# Tests
print(filter_even([1, 2, 3]))  # Expected: [2]
print(filter_even([0, 1, 2]))  # Expected: [0, 2]
print(filter_even([1]))        # Expected: []
print(filter_even([4, 5, 6]))  # Expected: [4, 6]
print(filter_even([]))         # Expected: []