#!/usr/bin/env python
# coding: utf-8

# ## Question 1
# Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
# Examples
# filter_list([1, 2, "a", "b"]) ➞ [1, 2]
# 
# filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]
# 
# filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
# 
# 
# 

# In[1]:


def filter_list(lst):
    return [x for x in lst if isinstance(x, int)]

# Example 1
print(filter_list([1, 2, "a", "b"]))  # Output: [1, 2]

# Example 2
print(filter_list([1, "a", "b", 0, 15]))  # Output: [1, 0, 15]

# Example 3
print(filter_list([1, 2, "aasf", "1", "123", 123]))  # Output: [1, 2, 123]


# ## Question 2
# The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.
# Examples
# reverse("Hello World") ➞ "DLROwOLLEh"
# 
# reverse("ReVeRsE") ➞ "eSrEvEr"
# 
# reverse("Radar") ➞ "RADAr"
# 
# 

# In[2]:


def filter_list(lst):
    return [x for x in lst if isinstance(x, int)]

# Example 1
print(filter_list([1, 2, "a", "b"]))  # Output: [1, 2]

# Example 2
print(filter_list([1, "a", "b", 0, 15]))  # Output: [1, 0, 15]

# Example 3
print(filter_list([1, 2, "aasf", "1", "123", 123]))  # Output: [1, 2, 123]


# ## Question 3
# You can assign variables from lists like this:
# lst = [1, 2, 3, 4, 5, 6]
# first = lst[0]
# middle = lst[1:-1]
# last = lst[-1]
# 
# print(first) ➞ outputs 1
# print(middle) ➞ outputs [2, 3, 4, 5]
# print(last) ➞ outputs 6
# With Python 3, you can assign variables from lists in a much more succinct way. Create variables first, middle and last from the given list using destructuring assignment (check the Resources tab for some examples), where:
# first  ➞ 1
# 
# middle➞ [2, 3, 4, 5]
# 
# last➞ 6
# Your task is to unpack the list writeyourcodehere into three variables, being first, middle, and last, with middle being everything in between the first and last element. Then print all three variables.
# 
# 

# In[3]:


def reverse(string):
    reversed_string = string[::-1]  # Reverse the string using slicing
    result = ""
    for char in reversed_string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result

# Example 1
print(reverse("Hello World"))  # Output: "DLROwOLLEh"

# Example 2
print(reverse("ReVeRsE"))  # Output: "eSrEvEr"

# Example 3
print(reverse("Radar"))  # Output: "RADAr"


# ## Question 4
# Write a function that calculates the factorial of a number recursively.
# Examples
# factorial(5) ➞ 120
# 
# factorial(3) ➞ 6
# 
# factorial(1) ➞ 1
# 
# factorial(0) ➞ 1

# In[5]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120


# ## Question 5
# Write a function that moves all elements of one type to the end of the list.
# Examples
# move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# # Move all the 1s to the end of the array.
# 
# move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]
# 
# move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]
# 
# 

# In[6]:


def move_to_end(lst, element):
    count = lst.count(element)  # Count the number of occurrences of the element
    lst = [x for x in lst if x != element]  # Create a new list without the element
    lst.extend([element] * count)  # Add the element to the end of the list count times
    return lst

# Test the function
print(move_to_end([1, 3, 2, 4, 4, 1], 1))  # Output: [3, 2, 4, 4, 1, 1]
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))  # Output: [7, 8, 1, 2, 3, 4, 9]
print(move_to_end(["a", "a", "a", "b"], "a"))  # Output: ["b", "a", "a", "a"]


# In[ ]:




