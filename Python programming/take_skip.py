def take(lst):
    return [lst[i] for i in range(0, len(lst), 2)]  # Take elements at indices 0, 2, 4, ...

def skip(lst):
    return [lst[i] for i in range(1, len(lst), 2)]  # Take elements at indices 1, 3, 5, ...

# Tests
if __name__ == "__main__":
    print(take([1, 2, 3, 4, 5]))  # Expected: [1, 3, 5]
    print(skip([1, 2, 3, 4, 5]))  # Expected: [2, 4]
    print(take([10, 20, 30, 40, 50, 60]))  # Expected: [10, 30, 50]
    print(skip([10, 20, 30, 40, 50, 60]))  # Expected: [20, 40, 60]
    print(take([]))  # Expected: []
    print(skip([]))  # Expected: []