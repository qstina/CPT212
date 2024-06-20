#!/usr/bin/env python
# coding: utf-8

# In[1]:


def boyer_moore_horspool(pattern, text):
    m = len(pattern)
    n = len(text)

    if m > n:
        return -1

    # Preprocess the pattern to create the shift table
    shift_table = {char: m for char in set(text)}  # Default shift for all characters in text
    for i in range(m - 1):
        shift_table[pattern[i]] = m - 1 - i

    # Start searching
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i  # Pattern found
        else:
            i += shift_table.get(text[i + m - 1], m)

    return -1  # Pattern not found

# Example usage:
text = "this is a simple example"
pattern = "example"
result = boyer_moore_horspool(pattern, text)
print(f"Pattern found at index: {result}" if result != -1 else "Pattern not found") #expected: 17


# In[ ]:




