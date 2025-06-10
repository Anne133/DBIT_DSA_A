def char_frequencies(t):
    freq = {}
    for char in t:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Example usage
text = "data structures and algorithms"
result = char_frequencies(text)
print(result)