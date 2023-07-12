#!/usr/bin/env python
# coding: utf-8

# ## Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.
# Examples
# equal(3, 4, 3) ➞ 2
# 
# equal(1, 1, 1) ➞ 3
# 
# equal(3, 4, 1) ➞ 0 
# Notes
# Your function must return 0, 2 or 3.
# 

# In[2]:


def equal(a, b, c):
    if a == b == c:
        return 3
    elif a == b or a == c or b == c:
        return 2
    else:
        return 0

# Test the function
print(equal(3, 4, 3))  # Output: 2
print(equal(1, 1, 1))  # Output: 3
print(equal(3, 4, 1))  # Output: 0


# ## 2. Write a function that converts a dictionary into a list of keys-values tuples.
# Examples
# dict_to_list({
#   "D": 1,
#   "B": 2,
#   "C": 3
# }) ➞ [("B", 2), ("C", 3), ("D", 1)]
# 
# dict_to_list({
#   "likes": 2,
#   "dislikes": 3,
#   "followers": 10
# }) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]
# Notes
# Return the elements in the list in alphabetical order.
# 

# In[7]:


def dict_to_list(dict_input):
  """
  This function converts a dictionary into a list of keys-values tuples.

  Args:
    dict_input: The dictionary to be converted.

  Returns:
    A list of keys-values tuples.
  """

  list_output = []
  for key, value in dict_input.items():
    tuple_output = (key, value)
    list_output.append(tuple_output)
  list_output.sort()
  return list_output


if __name__ == "__main__":
  dict_input = {
    "D": 1,
    "B": 2,
    "C": 3
  }
  list_output = dict_to_list(dict_input)
  print(list_output)

  dict_input = {
    "likes": 2,
    "dislikes": 3,
    "followers": 10
  }
  list_output = dict_to_list(dict_input)
  print(list_output)


# ## 3. Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
# Examples
# mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
# 
# mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
# 
# mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
# Notes
# All of the letters in the input list will always be lowercase.
# 

# In[9]:


import string

def mapping(letters):
  """
  This function creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.

  Args:
    letters: The list of letters to be used to create the dictionary.

  Returns:
    A dictionary with the (key, value) pairs being the (lower case, upper case) versions of a letter, respectively.
  """

  dictionary = {}
  for letter in letters:
    lowercase_letter = letter
    uppercase_letter = letter.upper()
    dictionary[lowercase_letter] = uppercase_letter
  return dictionary


if __name__ == "__main__":
  letters = ["p", "s"]
  dictionary = mapping(letters)
  print(dictionary)

  letters = ["a", "b", "c"]
  dictionary = mapping(letters)
  print(dictionary)

  letters = ["a", "v", "y", "z"]
  dictionary = mapping(letters)
  print(dictionary)


# ## 4. Write a function, that replaces all vowels in a string with a specified vowel.
# Examples
# vow_replace("apples and bananas", "u") ➞ "upplus und bununus"
# 
# vow_replace("cheese casserole", "o") ➞ "choosocossorolo"
# 
# vow_replace("stuffed jalapeno poppers", "e") ➞ "steffedjelepene peppers"
# Notes
# All words will be lowercase. Y is not considered a vowel
# 

# In[10]:


def vow_replace(string, vowel):
  """
  This function replaces all vowels in a string with a specified vowel.

  Args:
    string: The string to be modified.
    vowel: The vowel to be used to replace all vowels in the string.

  Returns:
    A string with all vowels replaced with the specified vowel.
  """

  vowels = "aeiou"
  new_string = ""
  for letter in string:
    if letter in vowels:
      new_string += vowel
    else:
      new_string += letter
  return new_string


if __name__ == "__main__":
  string = "apples and bananas"
  vowel = "u"
  new_string = vow_replace(string, vowel)
  print(new_string)

  string = "cheese casserole"
  vowel = "o"
  new_string = vow_replace(string, vowel)
  print(new_string)

  string = "stuffed jalapeno poppers"
  vowel = "e"
  new_string = vow_replace(string, vowel)
  print(new_string)


# ## 5. Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.
# Examples
# ascii_capitalize("to be or not to be!") ➞ "To Be oRNoT To Be!"
# 
# ascii_capitalize("THE LITTLE MERMAID") ➞ "THeLiTTLemeRmaiD"
# 
# ascii_capitalize("Oh what a beautiful morning.") ➞ "oHwHaT a BeauTiFuLmoRNiNg."
#  

# In[11]:


def ascii_capitalize(string):
  """
  This function takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.

  Args:
    string: The string to be modified.

  Returns:
    A string with all letters capitalized if their ASCII code is even and lowercased if their ASCII code is odd.
  """

  new_string = ""
  for letter in string:
    ascii_code = ord(letter)
    if ascii_code % 2 == 0:
      new_string += letter.upper()
    else:
      new_string += letter.lower()
  return new_string


if __name__ == "__main__":
  string = "to be or not to be!"
  new_string = ascii_capitalize(string)
  print(new_string)

  string = "THE LITTLE MERMAID"
  new_string = ascii_capitalize(string)
  print(new_string)

  string = "Oh what a beautiful morning."
  new_string = ascii_capitalize(string)
  print(new_string)


# In[ ]:




