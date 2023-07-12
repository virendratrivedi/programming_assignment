#!/usr/bin/env python
# coding: utf-8

# ## 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?

# In[2]:


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

# Test the function
n = int(input("Enter the number of terms in the Fibonacci sequence: "))
fib_sequence = fibonacci(n)
print("Fibonacci sequence:")
for num in fib_sequence:
    print(num)


# ## 2. Write a Python Program to Find Factorial of Number Using Recursion?

# In[3]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
n = int(input("Enter a non-negative integer: "))
result = factorial(n)
print("The factorial of", n, "is", result)


# ## 3. Write a Python Program to calculate your Body Mass Index?

# In[6]:


def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

# Test the function
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

print("Your Body Mass Index (BMI) is:", round(bmi, 2))


# ## 4. Write a Python Program to calculate the natural logarithm of any number?

# In[7]:


import math

number = float(input("Enter a number: "))

if number > 0:
    natural_log = math.log(number)
    print("The natural logarithm of", number, "is:", natural_log)
else:
    print("Invalid input. Please enter a positive number.")


# ## 5. Write a Python Program for cube sum of first n natural numbers

# In[8]:


def cube_sum(n):
    result = 0
    for i in range(1, n+1):
        result += i**3
    return result

# Test the function
n = int(input("Enter a positive integer: "))

if n > 0:
    cube_sum_result = cube_sum(n)
    print("The cube sum of the first", n, "natural numbers is:", cube_sum_result)
else:
    print("Invalid input. Please enter a positive integer.")


# In[ ]:




