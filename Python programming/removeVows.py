def remove_vowels(s):
    # TODO
    # Implement the function to remove vowels from the string s
    # and return the modified string.
    vowels = "aeiouAEIOU"
    result = ''.join([char for char in s if char not in vowels])
    return result
print(remove_vowels("you"))  # Output: "y"
print(remove_vowels("aeiou"))  # Output: ""
print(remove_vowels("hello"))  # Output: "hll"
print(remove_vowels("HELLO"))  # Output: "HLL"
print(remove_vowels("Python"))  # Output: "Pythn"
print(remove_vowels("umbrella")) # Output: "mbrll"
print(remove_vowels("aabaa"))  # Output: "bb"