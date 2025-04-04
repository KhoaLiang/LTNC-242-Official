def find_pairs(nums, target):
    def helper(nums, target, index):
        # Base case: If index reaches the end of the list, return an empty list
        if index >= len(nums):
            return []

        # Recursive case: Use a list comprehension to find pairs with the current element
        current = nums[index]
        pairs = [(current, nums[j]) for j in range(index + 1, len(nums)) if current + nums[j] == target]

        # Recur for the next index and combine results
        return pairs + helper(nums, target, index + 1)

    # Start the recursive process
    return helper(nums, target, 0)

# Tests
if __name__ == "__main__":
    print(find_pairs([1, 2, 3, 4, 5], 5))  # Expected: [(1, 4), (2, 3)]
    print(find_pairs([10, 20, 30, 40], 100))  # Expected: []
    print(find_pairs([1, 2, 3, 4, 3, 2, 1], 4))  # Expected: [(1, 3), (2, 2), (3, 1)]