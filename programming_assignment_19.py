#!/usr/bin/env python
# coding: utf-8

# ## Question1
# Create a function that takes a string and returns a string in which each character is repeated once.
# Examples
# double_char("String") ➞ "SSttrriinngg"
# 
# double_char("Hello World!") ➞ "HHeellllooWWoorrlldd!!"
# 
# double_char("1234!_ ") ➞ "11223344!!__  "
# 
# 

# In[1]:


def double_char(txt):
    result = ""
    for char in txt:
        result += char * 2
    return result

# Test the function
print(double_char("String"))  # Output: "SSttrriinngg"
print(double_char("Hello World!"))  # Output: "HHeelllloo  WWoorrlldd!!"
print(double_char("1234!_ "))  # Output: "11223344!!__  "


# ## Question2
# Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.
# Examples
# reverse(True) ➞ False
# 
# reverse(False) ➞ True
# 
# reverse(0) ➞ "boolean expected"
# 
# reverse(None) ➞ "boolean expected"

# In[2]:


def reverse(arg):
    if isinstance(arg, bool):
        return not arg
    else:
        return "boolean expected"

# Test the function
print(reverse(True))  # Output: False
print(reverse(False))  # Output: True
print(reverse(0))  # Output: "boolean expected"
print(reverse(None))  # Output: "boolean expected"


# ## Question3
# Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times. The paper starts off with a thickness of 0.5mm.
# Examples
# num_layers(1) ➞ "0.001m"
# # Paper folded once is 1mm (equal to 0.001m)
# 
# num_layers(4) ➞ "0.008m"
# # Paper folded 4 times is 8mm (equal to 0.008m)
# 
# num_layers(21) ➞ "1048.576m"
# # Paper folded 21 times is 1048576mm (equal to 1048.576m)
# 
# 
# 

# In[3]:


def num_layers(n):
    thickness_mm = 0.5 * (2 ** n)  # Calculate the thickness in mm
    thickness_m = thickness_mm / 1000  # Convert thickness to meters
    return "{:.3f}m".format(thickness_m)  # Format the result to 3 decimal places with 'm' unit

# Test the function
print(num_layers(1))  # Output: "0.001m"
print(num_layers(4))  # Output: "0.008m"
print(num_layers(21))  # Output: "1048.576m"


# ## Question4
# Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.
# Examples
# index_of_caps("eDaBiT") ➞ [1, 3, 5]
# 
# index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]
# 
# index_of_caps("determine") ➞ []
# 
# index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]
# 
# index_of_caps("sUn") ➞ [1]
# 
# 
# 

# In[4]:


def index_of_caps(word):
    indices = []  # List to store the indices of capital letters
    for i in range(len(word)):
        if word[i].isupper():
            indices.append(i)
    return indices

# Test the function
print(index_of_caps("eDaBiT"))  # Output: [1, 3, 5]
print(index_of_caps("eQuINoX"))  # Output: [1, 3, 4, 6]
print(index_of_caps("determine"))  # Output: []
print(index_of_caps("STRIKE"))  # Output: [0, 1, 2, 3, 4, 5]
print(index_of_caps("sUn"))  # Output: [1]


# ## Question5
# Using list comprehensions, create a function that finds all even numbers from 1 to the given number.
# Examples
# find_even_nums(8) ➞ [2, 4, 6, 8]
# 
# find_even_nums(4) ➞ [2, 4]
# 
# find_even_nums(2) ➞ [2]
# 
# 

# In[5]:


def find_even_nums(n):
    return [num for num in range(1, n+1) if num % 2 == 0]

# Test the function
print(find_even_nums(8))  # Output: [2, 4, 6, 8]
print(find_even_nums(4))  # Output: [2, 4]
print(find_even_nums(2))  # Output: [2]


# In[ ]:





# In[ ]:





# In[ ]:




