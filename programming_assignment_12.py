#!/usr/bin/env python
# coding: utf-8

# ## 1.Write a Python program to Extract Unique values dictionary values?
# 
# 

# In[1]:


def extract_unique_values(dictionary):
    unique_values = set(dictionary.values())
    return unique_values

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
result = extract_unique_values(my_dict)
print("Unique values:", result)


# ## 2. Write a Python program to find the sum of all items in a dictionary?
# 

# In[2]:


def sum_dictionary_items(dictionary):
    return sum(dictionary.values())

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
result = sum_dictionary_items(my_dict)
print("Sum of dictionary items:", result)


# ## 3. Write a Python program to Merging two Dictionaries?
# 

# In[3]:


def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# Example usage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = merge_dictionaries(dict1, dict2)
print("Merged dictionary:", merged_dict)


# ## 4. Write a Python program to convert key-values list to flat dictionary?
# 

# In[4]:


def convert_to_flat_dictionary(key_value_list):
    flat_dictionary = {key: value for key, value in key_value_list}
    return flat_dictionary

# Example usage:
key_value_list = [("a", 1), ("b", 2), ("c", 3)]
flat_dict = convert_to_flat_dictionary(key_value_list)
print("Flat Dictionary:", flat_dict)


# ## 5. Write a Python program to insertion at the beginning in OrderedDict?
# 

# In[5]:


from collections import OrderedDict

def insert_at_beginning(ordered_dict, key, value):
    ordered_dict[key] = value
    ordered_dict.move_to_end(key, last=False)

# Example usage:
ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print("Original OrderedDict:", ordered_dict)

insert_at_beginning(ordered_dict, 'x', 10)
print("OrderedDict after insertion:", ordered_dict)


# ## 6. Write a Python program to check order of character in string using OrderedDict()?
# 

# In[6]:


from collections import OrderedDict

def check_character_order(string):
    ordered_dict = OrderedDict()

    for char in string:
        if char in ordered_dict:
            continue
        ordered_dict[char] = None

    return ''.join(ordered_dict.keys())

# Example usage:
input_string = "hello world"
result = check_character_order(input_string)
print("Order of characters:", result)


# ## 7. Write a Python program to sort Python Dictionaries by Key or Value?

# In[7]:


def sort_dictionary_by_key(dictionary):
    sorted_dict = dict(sorted(dictionary.items()))
    return sorted_dict

# Example usage:
my_dict = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
sorted_by_key = sort_dictionary_by_key(my_dict)
print("Sorted by Key:", sorted_by_key)


# In[ ]:




