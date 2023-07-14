#!/usr/bin/env python
# coding: utf-8

# ## 1. Write a Python program to find words which are greater than given length k?
# 

# In[1]:


def find_words_greater_than_length(words, k):
    result = []
    for word in words:
        if len(word) > k:
            result.append(word)
    return result

# Example usage:
word_list = ["apple", "banana", "kiwi", "orange", "grapefruit"]
k = 5
result = find_words_greater_than_length(word_list, k)
print(f"Words greater than length {k}: {result}")


# ## 2. Write a Python program for removing i-th character from a string?
# 

# In[2]:


def remove_character(string, i):
    if i < 0 or i >= len(string):
        return string

    return string[:i] + string[i+1:]

# Example usage:
input_string = "Hello, World!"
index = 7
result = remove_character(input_string, index)
print(f"String after removing character at index {index}: {result}")


# ## 3. Write a Python program to split and join a string?
# 
# 

# In[3]:


def split_and_join(string, separator):
    # Split the string into a list of substrings
    split_list = string.split(separator)
    
    # Join the list of substrings into a single string using the specified separator
    joined_string = separator.join(split_list)
    
    return joined_string

# Example usage:
input_string = "Hello, World!"
separator = ","
result = split_and_join(input_string, separator)
print(f"Joined string: {result}")


# ## 4. Write a Python to check if a given string is binary string or not?
# 

# In[4]:


def is_binary_string(string):
    for char in string:
        if char != '0' and char != '1':
            return False
    return True

# Example usage:
input_string = "101010"
result = is_binary_string(input_string)
if result:
    print(f"The string '{input_string}' is a binary string.")
else:
    print(f"The string '{input_string}' is not a binary string.")


# ## 5. Write a Python program to find uncommon words from two Strings?
# 

# In[5]:


def find_uncommon_words(string1, string2):
    # Split the strings into words
    words1 = string1.split()
    words2 = string2.split()

    # Create sets of unique words
    unique_words1 = set(words1)
    unique_words2 = set(words2)

    # Find the uncommon words
    uncommon_words = unique_words1.symmetric_difference(unique_words2)

    return uncommon_words

# Example usage:
string1 = "Hello world, how are you?"
string2 = "Hello Python, how is it going?"
uncommon_words = find_uncommon_words(string1, string2)
print("Uncommon words:", uncommon_words)


# ## 6. Write a Python to find all duplicate characters in string?

# In[6]:


def find_duplicate_characters(string):
    char_count = {}
    duplicate_chars = []

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        if count > 1:
            duplicate_chars.append(char)

    return duplicate_chars

# Example usage:
input_string = "Hello, World!"
result = find_duplicate_characters(input_string)
print("Duplicate characters:", result)


# ## 7. Write a Python Program to check if a string contains any special character?

# In[7]:


def contains_special_characters(string):
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    for char in string:
        if char in special_characters:
            return True
    return False

# Example usage:
input_string = "Hello, World!"
result = contains_special_characters(input_string)
if result:
    print("The string contains special characters.")
else:
    print("The string does not contain special characters.")


# In[ ]:




