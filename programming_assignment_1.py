#!/usr/bin/env python
# coding: utf-8

# # 1. Write a Python program to print "Hello Python"?

# In[1]:


print("Hello Python")


# # 2. Write a Python program to do arithmetical operations addition and division.?

# In[2]:


a=10
b=5
add=a+b
div=a/b
print(add)
print(div)


# # 3.Write a Python program to find the area of a triangle?

# In[4]:


a = 5
b = 6
c = 7

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


# # 4.Write a Python program to swap two variables?

# In[5]:


a=10
b=20
# Swap without third variables
print("Before swipe a:",a)
print("Before swipe b:",b)
a=a+b  
b=a-b  
a=a-b 

print("After swipe a:",a)
print("After swipe b:",b)


# # 5.Write a Python program to generate a random number?

# In[16]:


import random

print(random.randint(0,100))


# In[ ]:





# In[ ]:




