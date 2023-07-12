#!/usr/bin/env python
# coding: utf-8

# ## 1.Write a Python Program to Add Two Matrices?
# 

# In[7]:


def add_matrices(matrix_1, matrix_2):
  """
  This function adds two matrices.

  Args:
    matrix_1: The first matrix.
    matrix_2: The second matrix.

  Returns:
    The sum of the two matrices.
  """

  if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
    raise ValueError("The two matrices must have the same dimensions.")

  new_matrix = []
  for i in range(len(matrix_1)):
    row = []
    for j in range(len(matrix_1[0])):
      row.append(matrix_1[i][j] + matrix_2[i][j])
    new_matrix.append(row)

  return new_matrix


if __name__ == "__main__":
  matrix_1 = [[1, 2, 3], [4, 5, 6]]
  matrix_2 = [[7, 8, 9], [10, 11, 12]]
  new_matrix = add_matrices(matrix_1, matrix_2)
  print(new_matrix)


# ## 2. Write a Python Program to Multiply Two Matrices?

# In[8]:


def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        return None

    result = [[0] * cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Test the function
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[10, 11],
           [12, 13],
           [14, 15]]

result_matrix = multiply_matrices(matrix1, matrix2)

if result_matrix is not None:
    print("Resultant Matrix:")
    for row in result_matrix:
        print(row)
else:
    print("Matrix multiplication not possible.")


# ## 3. Write a Python Program to Transpose a Matrix?
# 

# In[9]:


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix with swapped dimensions
    transposed_matrix = [[0] * rows for _ in range(cols)]

    # Copy elements to the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

# Test the function
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed = transpose_matrix(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed:
    print(row)


# ## 4.	Write a Python Program to Sort Words in Alphabetic Order?
# 
# 

# In[10]:


def sort_words_alphabetically(sentence):
    words = sentence.split()
    sorted_words = sorted(words)
    return sorted_words

# Test the function
sentence = input("Enter a sentence: ")

sorted_words = sort_words_alphabetically(sentence)

print("Words in alphabetical order:")
for word in sorted_words:
    print(word)


# ## 5. Write a Python Program to Remove Punctuation From a String?

# In[12]:


import string

def remove_punctuation(input_string):
    # Create a translation table with punctuation characters mapped to None
    translator = str.maketrans("", "", string.punctuation)
    # Use the translation table to remove punctuation from the string
    no_punct = input_string.translate(translator)
    return no_punct

# Test the function
input_string = input("Enter a string: ")

no_punct_string = remove_punctuation(input_string)

print("String without punctuation:", no_punct_string)


# In[6]:





# In[ ]:




