#!/usr/bin/env python
# coding: utf-8

# ## 1. Write a Python program to check if the given number is a Disarium Number?
# 
# 

# In[6]:


def is_disarium_number(number):
    digit_power_sum = 0
    position = 1
    temp_number = number

    # Calculate the sum of the digits raised to their respective positions
    while temp_number > 0:
        digit = temp_number % 10
        digit_power_sum += digit ** position
        position += 1
        temp_number //= 10

    return digit_power_sum == number

# Example usage:
number = 175
result = is_disarium_number(number)
if result:
    print(f"{number} is a Disarium number.")
else:
    print(f"{number} is not a Disarium number.")


# ## 2. Write a Python program to print all disarium numbers between 1 to 100?
# 

# In[5]:


def is_disarium_number(number):
    digit_power_sum = 0
    position = 1
    temp_number = number

    # Calculate the sum of the digits raised to their respective positions
    while temp_number > 0:
        digit = temp_number % 10
        digit_power_sum += digit ** position
        position += 1
        temp_number //= 10

    return digit_power_sum == number

def print_disarium_numbers():
    print("Disarium numbers between 1 and 100:")
    for num in range(1, 101):
        if is_disarium_number(num):
            print(num, end=" ")

# Example usage:
print_disarium_numbers()


# ## 3. Write a Python program to check if the given number is Happy Number?
# 

# In[4]:


def is_happy_number(number):
    seen_numbers = set()

    while number != 1 and number not in seen_numbers:
        seen_numbers.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))

    return number == 1

# Example usage:
number = 19
result = is_happy_number(number)
if result:
    print(f"{number} is a happy number.")
else:
    print(f"{number} is not a happy number.")


# ## 4. Write a Python program to print all happy numbers between 1 and 100?
# 

# In[3]:


def is_happy_number(number):
    seen_numbers = set()

    while number != 1 and number not in seen_numbers:
        seen_numbers.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))

    return number == 1

def print_happy_numbers():
    print("Happy numbers between 1 and 100:")
    for num in range(1, 101):
        if is_happy_number(num):
            print(num, end=" ")

# Example usage:
print_happy_numbers()


# ## 5. Write a Python program to determine whether the given number is a Harshad Number?
# 

# In[2]:


def is_harshad_number(number):
    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in str(number))

    # Check if the number is divisible by the sum of its digits
    return number % digit_sum == 0

# Example usage:
number = 18
result = is_harshad_number(number)
if result:
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")


# ## 6. Write a Python program to print all pronic numbers between 1 and 100?

# In[1]:


def is_pronic_number(n):
    for i in range(1, int(n ** 0.5) + 1):
        if i * (i + 1) == n:
            return True
    return False

def print_pronic_numbers():
    print("Pronic numbers between 1 and 100:")
    for num in range(1, 101):
        if is_pronic_number(num):
            print(num, end=" ")

# Example usage:
print_pronic_numbers()


# In[ ]:




