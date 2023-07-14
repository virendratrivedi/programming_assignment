#!/usr/bin/env python
# coding: utf-8

# ## Question1. Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.
# Examples
# evenly_divisible(1, 10, 20) ➞ 0
# # No number between 1 and 10 can be evenly divided by 20.
# 
# evenly_divisible(1, 10, 2) ➞ 30
# # 2 + 4 + 6 + 8 + 10 = 30
# 
# evenly_divisible(1, 10, 3) ➞ 18
# # 3 + 6 + 9 = 18
# 

# In[1]:


def evenly_divisible(a, b, c):
    total = 0
    for num in range(a, b + 1):
        if num % c == 0:
            total += num
    return total

# Example 1
print(evenly_divisible(1, 10, 20))  # Output: 0

# Example 2
print(evenly_divisible(1, 10, 2))  # Output: 30

# Example 3
print(evenly_divisible(1, 10, 3))  # Output: 18


# ## Question2. Create a function that returns True if a given inequality expression is correct and False otherwise.
# Examples
# correct_signs("3 < 7 < 11") ➞ True
# 
# correct_signs("13 > 44 > 33 > 1") ➞ False
# 
# correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
# 

# In[2]:


def correct_signs(expression):
    return eval(expression)

# Example 1
print(correct_signs("3 < 7 < 11"))  # Output: True

# Example 2
print(correct_signs("13 > 44 > 33 > 1"))  # Output: False

# Example 3
print(correct_signs("1 < 2 < 6 < 9 > 3"))  # Output: True


# ## Question3.Create a function that replaces all the vowels in a string with a specified character.
# Examples
# replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"
# 
# replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"
# 
# replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
# 

# In[3]:


def replace_vowels(string, char):
    vowels = "aeiouAEIOU"
    result = ""
    for letter in string:
        if letter in vowels:
            result += char
        else:
            result += letter
    return result

# Example 1
print(replace_vowels("the aardvark", "#"))  # Output: "th# ##rdv#rk"

# Example 2
print(replace_vowels("minnie mouse", "?"))  # Output: "m?nn?? m??s?"

# Example 3
print(replace_vowels("shakespeare", "*"))  # Output: "sh*k*sp**r*"


# ## Question4. Write a function that calculates the factorial of a number recursively.
# Examples
# factorial(5) ➞ 120
# 
# factorial(3) ➞ 6
# 
# factorial(1) ➞ 1
# 
# factorial(0) ➞ 1
# 
# 

# In[4]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example 1
print(factorial(5))  # Output: 120

# Example 2
print(factorial(3))  # Output: 6

# Example 3
print(factorial(1))  # Output: 1

# Example 4
print(factorial(0))  # Output: 1


# ## Question 5
# Hamming distance is the number of characters that differ between two strings.
# To illustrate:
# String1: "abcbba"
# String2: "abcbda"
# 
# Hamming Distance: 1 - "b" vs. "d" is the only difference.
# Create a function that computes the hamming distance between two strings.
# Examples
# hamming_distance("abcde", "bcdef") ➞ 5
# 
# hamming_distance("abcde", "abcde") ➞ 0
# 
# hamming_distance("strong", "strung") ➞ 1
# 
# 

# In[5]:


def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return "Error: Strings must have the same length"
    
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    
    return distance

# Example 1
print(hamming_distance("abcde", "bcdef"))  # Output: 5

# Example 2
print(hamming_distance("abcde", "abcde"))  # Output: 0

# Example 3
print(hamming_distance("strong", "strung"))  # Output: 1


# In[ ]:




