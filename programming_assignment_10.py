#!/usr/bin/env python
# coding: utf-8

# ## 1. Write a Python program to find sum of elements in list?
# 

# In[1]:


def sum_of_elements(lst):
    return sum(lst)

# Example usage:
my_list = [1, 2, 3, 4, 5]
result = sum_of_elements(my_list)
print(f"The sum of elements in the list is: {result}")


# ## 2. Write a Python program to  Multiply all numbers in the list?
# 

# In[2]:


def multiply_numbers(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Example usage:
my_list = [1, 2, 3, 4, 5]
result = multiply_numbers(my_list)
print(f"The product of all numbers in the list is: {result}")


# ## 3. Write a Python program to find smallest number in a list?
# 

# In[3]:


def find_smallest_number(lst):
    return min(lst)

# Example usage:
my_list = [5, 2, 8, 1, 9]
result = find_smallest_number(my_list)
print(f"The smallest number in the list is: {result}")


# ## 4. Write a Python program to find largest number in a list?
# 

# In[4]:


def find_smallest_number(lst):
    return max(lst)

# Example usage:
my_list = [5, 2, 8, 1, 9]
result = find_smallest_number(my_list)
print(f"The lasrge number in the list is: {result}")


# ## 5. Write a Python program to find second largest number in a list?
# 

# In[5]:


def find_second_largest_number(lst):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[1]

# Example usage:
my_list = [5, 2, 8, 1, 9]
result = find_second_largest_number(my_list)
print(f"The second largest number in the list is: {result}")


# ## 6. Write a Python program to find N largest elements from a list?
# 

# In[6]:


import heapq

def find_n_largest_elements(lst, n):
    return heapq.nlargest(n, lst)

# Example usage:
my_list = [5, 2, 8, 1, 9]
n = 3
result = find_n_largest_elements(my_list, n)
print(f"The {n} largest elements in the list are: {result}")


# ## 7. Write a Python program to print even numbers in a list?
# 

# In[7]:


def print_even_numbers(lst):
    print("Even numbers in the list:")
    for num in lst:
        if num % 2 == 0:
            print(num)

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_even_numbers(my_list)


# ## 8. Write a Python program to print odd numbers in a List?
# 

# In[8]:


def print_odd_numbers(lst):
    print("Odd numbers in the list:")
    for num in lst:
        if num % 2 != 0:
            print(num)

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_odd_numbers(my_list)


# ## 9. Write a Python program to Remove empty List from List?
# 

# In[9]:


def remove_empty_lists(lst):
    return [sublist for sublist in lst if sublist]

# Example usage:
my_list = [1, 2, [], 3, [], 4, 5, [], 6, [], 7, 8, [], 9, []]
result = remove_empty_lists(my_list)
print(f"The list after removing empty lists: {result}")


# ## 10. Write a Python program to Cloning or Copying a list?
# 
# 

# In[10]:


def clone_list(lst):
    # Using slicing
    cloned_list_slicing = lst[:]

    # Using list() function
    cloned_list_list = list(lst)

    return cloned_list_slicing, cloned_list_list

# Example usage:
original_list = [1, 2, 3, 4, 5]
cloned_list_slicing, cloned_list_list = clone_list(original_list)

print(f"Original list: {original_list}")
print(f"Cloned list (using slicing): {cloned_list_slicing}")
print(f"Cloned list (using list() function): {cloned_list_list}")


# ## 11. Write a Python program to Count occurrences of an element in a list?

# In[11]:


def count_occurrences(lst, element):
    return lst.count(element)

# Example usage:
my_list = [1, 2, 3, 4, 2, 2, 5, 6, 2]
element = 2
occurrences = count_occurrences(my_list, element)
print(f"The element {element} occurs {occurrences} times in the list.")


# In[ ]:




