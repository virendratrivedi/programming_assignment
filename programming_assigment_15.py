#!/usr/bin/env python
# coding: utf-8

# ## Question 1:
# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 100
# Then, the output of the program should be:
# 0,35,70
# 
# 

# In[2]:


def divisible_by_5_and_7(n):
    for i in range(n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

# Get input from console
n = int(input("Enter a number: "))

result = ",".join(str(num) for num in divisible_by_5_and_7(n))
print(result)


# ## Question 2:
# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10
# 

# In[3]:


def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

# Get input from console
n = int(input("Enter a number: "))

result = ",".join(str(num) for num in even_numbers(n))
print(result)


# Question 3:
# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
# Example:
# If the following n is given as input to the program:
# 7
# 
# Then, the output of the program should be:
# 0,1,1,2,3,5,8,13
# 
# 

# In[8]:


def fibonacci_sequence(n):
    sequence = [0, 1]  # Initialize the sequence with the first two numbers

    # Generate the Fibonacci sequence using list comprehension
    sequence += [sequence[-1] + sequence[-2] for _ in range(n-1)]

    return sequence

# Get input from console
n = int(input("Enter a number: "))

# Generate and print the Fibonacci sequence
result = fibonacci_sequence(n)
print(",".join(str(num) for num in result))


# Question 4:
# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# john
# 
# 

# In[10]:


def get_username(email):
    parts = email.split("@")
    username = parts[0]
    return username

# Get input from console
email = input("Enter an email address: ")

# Extract and print the username
username = get_username(email)
print(username)


# ## Question 5:
# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
# 
# 

# In[13]:


class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length ** 2
# Create a square object with length 5
square = Square(5)

# Calculate and print the area of the square
print(square.area())  # Output: 25


# In[ ]:




