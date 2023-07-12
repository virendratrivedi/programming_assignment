#!/usr/bin/env python
# coding: utf-8

# ## 1. Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.
# Examples
# is_symmetrical(7227) ➞ True
# 
# is_symmetrical(12567) ➞ False
# 
# is_symmetrical(44444444) ➞ True
# 
# is_symmetrical(9939) ➞ False
# 
# is_symmetrical(1112111) ➞ True
# 

# In[1]:


def is_symmetrical(num):
    num_str = str(num)
    return num_str == num_str[::-1]

# Test the function
print(is_symmetrical(7227))  # Output: True
print(is_symmetrical(12567))  # Output: False
print(is_symmetrical(44444444))  # Output: True
print(is_symmetrical(9939))  # Output: False
print(is_symmetrical(1112111))  # Output: True


# ## 2. Given a string of numbers separated by a comma and space, return the product of the numbers.
# Examples
# multiply_nums("2, 3") ➞ 6
# 
# multiply_nums("1, 2, 3, 4") ➞ 24
# 
# multiply_nums("54, 75, 453, 0") ➞ 0
# 
# multiply_nums("10, -2") ➞ -20
# 

# In[2]:


def multiply_nums(nums):
    num_list = [int(num) for num in nums.split(", ")]
    product = 1
    for num in num_list:
        product *= num
    return product

# Test the function
print(multiply_nums("2, 3"))  # Output: 6
print(multiply_nums("1, 2, 3, 4"))  # Output: 24
print(multiply_nums("54, 75, 453, 0"))  # Output: 0
print(multiply_nums("10, -2"))  # Output: -20


# ## 3. Create a function that squares every digit of a number.
# Examples
# square_digits(9119) ➞ 811181
# 
# square_digits(2483) ➞ 416649
# 
# square_digits(3212) ➞ 9414
# Notes
# The function receives an integer and must return an integer.
# 

# In[3]:


def square_digits(num):
    result = ""
    for digit in str(num):
        square = int(digit) ** 2
        result += str(square)
    return int(result)

# Test the function
print(square_digits(9119))  # Output: 811181
print(square_digits(2483))  # Output: 416649
print(square_digits(3212))  # Output: 9414


# ## 4. Create a function that sorts a list and removes all duplicate items from it.
# Examples
# setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
# 
# setify([4, 4, 4, 4]) ➞ [4]
# 
# setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
# 
# setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]
# 

# In[4]:


def setify(lst):
    return sorted(list(set(lst)))

# Test the function
print(setify([1, 3, 3, 5, 5]))  # Output: [1, 3, 5]
print(setify([4, 4, 4, 4]))  # Output: [4]
print(setify([5, 7, 8, 9, 10, 15]))  # Output: [5, 7, 8, 9, 10, 15]
print(setify([3, 3, 3, 2, 1]))  # Output: [1, 2, 3]


# ## 5. Create a function that returns the mean of all digits.
# Examples
# mean(42) ➞ 3
# 
# mean(12345) ➞ 3
# 
# mean(666) ➞ 6
# Notes
# •	The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
# •	The mean will always be an integer.
# 

# In[5]:


def mean(num):
    digits = [int(digit) for digit in str(num)]
    return sum(digits) // len(digits)

# Test the function
print(mean(42))  # Output: 3
print(mean(12345))  # Output: 3
print(mean(666))  # Output: 6


# In[ ]:




