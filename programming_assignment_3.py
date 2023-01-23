#!/usr/bin/env python
# coding: utf-8

# # 1.Write a Python Program to Check if a Number is Positive, Negative or Zero

# In[5]:


myNumber=int(input("plz enter number"))
if myNumber==0:
    print("This is Zero")
elif myNumber>0:
    print("This is positive number")
else:
    print("This is negative number")


# # 2.Write a Python Program to Check if a Number is Odd or Even?

# In[7]:


myNumber=int(input("plz enter number"))
if myNumber%2==0:
    print("even")
else:
    print("odd")
    


# # 3. Write a Python Program to Check Leap Year

# In[12]:


year = int(input("Enter a year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print("{} is a leap year".format(year))

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

else:
    print("{0} is not a leap year".format(year))


# # 4.Write a Python Program to Check Prime Number

# In[41]:


pnum = int(input("Enter a year: "))
#flag=False
if pnum==1:
    print(pnum, "is not a prime number")
else:
    for i in range(2,pnum):
        if pnum%i==0:
            print(pnum, "is not a prime number")
            break
        else:
            print(pnum, "is a prime number")
            break
            
            


# # 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[38]:


def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2,n):
            if n % i == 0:
                status = False
    return status

for n in range(1,10000):
    if is_prime(n):
        if n==97:
            print (n)
        else:
            print (n,",",)
        
    
        


# In[ ]:




