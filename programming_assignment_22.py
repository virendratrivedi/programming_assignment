#!/usr/bin/env python
# coding: utf-8

# ## Question1
# Create a function that takes three parameters where:
# •	x is the start of the range (inclusive).
# •	y is the end of the range (inclusive).
# •	n is the divisor to be checked against.
# Return an ordered list with numbers in the range that are divisible by the third parameter n. Return an empty list if there are no numbers that are divisible by n.
# Examples
# list_operation(1, 10, 3) ➞ [3, 6, 9]
# 
# list_operation(7, 9, 2) ➞ [8]
# 
# list_operation(15, 20, 7) ➞ []
# 
# 

# In[2]:


def list_operation(x, y, n):
    # Use list comprehension to generate a list of numbers divisible by n
    divisible_numbers = [num for num in range(x, y + 1) if num % n == 0]
    return divisible_numbers

# Test the function
print(list_operation(1, 10, 3))  # Output: [3, 6, 9]
print(list_operation(7, 9, 2))  # Output: [8]
print(list_operation(15, 20, 7))  # Output: []


# ## Question2
# Create a function that takes in two lists and returns True if the second list follows the first list by one element, and False otherwise. In other words, determine if the second list is the first list shifted to the right by 1.
# Examples
# simon_says([1, 2], [5, 1]) ➞ True
# 
# simon_says([1, 2], [5, 5]) ➞ False
# 
# simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True
# 
# simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False
# Notes
# •	Both input lists will be of the same length, and will have a minimum length of 2.
# •	The values of the 0-indexed element in the second list and the n-1th indexed element in the first list do not matter.
# 
# 

# In[3]:


def simon_says(lst1, lst2):
    # Check if lst2 is the same as lst1 shifted to the right by 1
    return lst2[1:] == lst1[:-1]

# Test the function
print(simon_says([1, 2], [5, 1]))  # Output: True
print(simon_says([1, 2], [5, 5]))  # Output: False
print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))  # Output: True
print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))  # Output: False


# ## Question3
# A group of friends have decided to start a secret society. The name will be the first letter of each of their names, sorted in alphabetical order.
# Create a function that takes in a list of names and returns the name of the secret society.
# Examples
# society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"
# 
# society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"
# 
# society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])
# 
# 

# In[4]:


def society_name(names):
    # Extract the first letter from each name and sort them
    society_name = ''.join(sorted(name[0] for name in names))
    return society_name

# Test the function
print(society_name(["Adam", "Sarah", "Malcolm"]))  # Output: "AMS"
print(society_name(["Harry", "Newt", "Luna", "Cho"]))  # Output: "CHLN"
print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))  # Output: "CJMPRR"


# ## Question4
# An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
# Examples
# is_isogram("Algorism") ➞ True
# 
# is_isogram("PasSword") ➞ False
# # Not case sensitive.
# 
# is_isogram("Consecutive") ➞ False
# Notes
# •	Ignore letter case (should not be case sensitive).
# •	All test cases contain valid one word strings.
# 
# 

# In[5]:


def is_isogram(word):
    # Convert the word to lowercase to ignore letter case
    word = word.lower()
    # Check if the length of the word is equal to the number of unique characters
    return len(word) == len(set(word))

# Test the function
print(is_isogram("Algorism"))  # Output: True
print(is_isogram("PasSword"))  # Output: False
print(is_isogram("Consecutive"))  # Output: False


# ## Question5
# Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.
# Examples
# is_in_order("abc") ➞ True
# 
# is_in_order("edabit") ➞ False
# 
# is_in_order("123") ➞ True
# 
# is_in_order("xyzz") ➞ True
# Notes
# You don't have to handle empty strings.
# 
# 

# In[6]:


def is_in_order(txt):
    # Sort the characters of the string
    sorted_txt = ''.join(sorted(txt))
    # Check if the sorted string is equal to the original string
    return sorted_txt == txt

# Test the function
print(is_in_order("abc"))  # Output: True
print(is_in_order("edabit"))  # Output: False
print(is_in_order("123"))  # Output: True
print(is_in_order("xyzz"))  # Output: True


# In[ ]:




