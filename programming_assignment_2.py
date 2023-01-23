#!/usr/bin/env python
# coding: utf-8

# # 1.Write a Python program to convert kilometers to miles?

# In[3]:


def convert_kilometer_to_miles(myInput):
    miles = 0.62*myInput
    print("miles value:",miles)
    
print("Please write kilometer value that you want convert in miles")
myInput=int(input())
convert_kilometer_to_miles(myInput)




# # 2. Write a Python program to convert Celsius to Fahrenheit?

# In[5]:


def convert_celsius_to_farrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    print("fahrenheit value:",fahrenheit)
    
print("Please write celsius value that you want convert in fahrenheit")
myInput=int(input())
convert_celsius_to_farrenheit(myInput)


# # 3. Write a Python program to display calendar?

# In[7]:


import calendar
# To take month and year input from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


# # 4.Write a Python program to solve quadratic equation?

# In[9]:


import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
# calculate the discriminant  
d = (b**2) - (4*a*c)  
  
# find two solutions  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))   


# # 5. Write a Python program to swap two variables without temp variable?

# In[22]:


x = 10
y = 20

print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

# code to swap 'x' and 'y'
x, y = y, x


print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)


# In[27]:


cwd


# In[ ]:




