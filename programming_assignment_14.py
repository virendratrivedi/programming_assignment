#!/usr/bin/env python
# coding: utf-8

# ## Question 1:
# 
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
# 
# 

# In[1]:


class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generate_numbers(self):
        for num in range(self.n + 1):
            if num % 7 == 0:
                yield num


# Example usage
n = 50
divisible_by_seven = DivisibleBySeven(n)

for num in divisible_by_seven.generate_numbers():
    print(num)


# ## Question 2:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# 
# Suppose the following input is supplied to the program:
# 
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# 
# Then, the output should be:
# 
# 2:2
# 
# 3.:1
# 
# 3?:1
# 
# New:1
# 
# Python:5
# 
# Read:1
# 
# and:1
# 
# between:1
# 
# choosing:1
# 
# or:2
# 
# to:1
# 
# 

# In[2]:


def word_frequency(sentence):
    word_count = {}
    words = sentence.split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    sorted_words = sorted(word_count.items())

    for word, count in sorted_words:
        print(f"{word}:{count}")


# Example usage
input_sentence = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
word_frequency(input_sentence)


# ## Question 3:
# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
# 

# In[3]:


class Person:
    def getGender(self):
        pass


class Male(Person):
    def getGender(self):
        print("Male")


class Female(Person):
    def getGender(self):
        print("Female")


# Example usage
person1 = Male()
person1.getGender()  # Output: Male

person2 = Female()
person2.getGender()  # Output: Female


# ## Question 4:
# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
# 

# In[4]:


subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

sentences = []

for subject in subjects:
    for verb in verbs:
        for obj in objects:
            sentence = subject + " " + verb + " " + obj
            sentences.append(sentence)

# Print the generated sentences
for sentence in sentences:
    print(sentence)


# ## Question 5:
# Please write a program to compress and decompress the string "hello world!helloworld!helloworld!hello world!".
# 

# In[5]:


import zlib

def compress_string(string):
    compressed_data = zlib.compress(bytes(string, 'utf-8'))
    return compressed_data

def decompress_string(compressed_data):
    decompressed_string = zlib.decompress(compressed_data)
    return decompressed_string.decode('utf-8')

# Original string
original_string = "hello world!helloworld!helloworld!hello world!"
print("Original string:", original_string)

# Compress the string
compressed_data = compress_string(original_string)
print("Compressed data:", compressed_data)

# Decompress the string
decompressed_string = decompress_string(compressed_data)
print("Decompressed string:", decompressed_string)


# ## Question 6:
# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
# 

# In[6]:


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage
sorted_list = [2, 5, 7, 12, 18, 20, 23]
target = 12

index = binary_search(sorted_list, target)

if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found in the list")


# In[ ]:




