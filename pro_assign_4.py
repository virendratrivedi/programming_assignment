#!/usr/bin/env python
# coding: utf-8

# ## Qu:- 1. Write a Python Program to Find the Factorial of a Number?

# In[6]:


a=int(input("enter number for Factorial"))
result=a*(a+1)/2
print("Factorial of number is::",result)


# ## 2. Write a Python Program to Display the multiplication Table?

# In[11]:


a=int(input("enter number for Table"))
for i in range(1,11):
    result=a*i
    print(result)


# ## 3 Write a Python Program to Print the Fibonacci sequence?

# In[17]:


first =0
second = 1
print(first)
print(second)
for i in range(10):
    result=first+second
    print(result)
    first=second
    second=result
    
    


# ## 4 Write a Python Program to Check Armstrong Number?

# In[57]:


number=int(input("Enter Any number for Armstrong"))
orig=number
sum=0

while(number>0):
    sum=sum+(number%10)*(number%10)*(number%10)
    number=number//10
    
print(sum)
if orig==sum:
    print("Armstrong")
else:
    print("Not Armstong")
    


# ## 5.Write a Python Program to Find Armstrong Number in an Interval?

# In[67]:


lower=int(input("Enter the lower limit"))
upper=int(input("Enter the upper limit"))

for num in range(lower,upper+1):
    order=len(str(num))
    sum=0
    temp=num
    while(temp>0):
        digit=temp%10
        sum=sum+digit **order
        temp=temp//10
    
    if num==sum:
        print("Armstrong",sum)
        
    


# ## 6. Write a Python Program to Find the Sum of Natural Numbers?

# In[69]:


lower=int(input("Enter the lower limit"))
upper=int(input("Enter the upper limit"))
sum=0
for num in range(lower,upper+1):
    sum=sum+num
print("The Total:",sum)    
    


# In[ ]:




