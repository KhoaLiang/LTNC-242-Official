def filter_by_length(words, n):
    # """
    # Return words with exactly n characters.
    
    # :param words: List of strings.
    # :param n: Integer representing the desired word length.
    # :return: List of words with exactly n characters.
    # """
    return [word for word in words if len(word) == n]

print(filter_by_length(["apple", "banana", "pear", "kiwi", "peach"], 5))  # Expected: ['apple', 'peach']
print(filter_by_length(["dog", "cat", "fish", "bird"], 6))                # Expected: []
print(filter_by_length(["one", "two", "six"], 3))                        # Expected: ['one', 'two', 'six']
print(filter_by_length([], 4))                                           # Expected: []
print(filter_by_length(["hello", "world"], 10))                          # Expected: []