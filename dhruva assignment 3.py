#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Questions 1:
# Create a numpy array starting from 2 till 50 with a stepsize of 3.

import numpy as np  # importing numpy pkg.

my_array = np.arange(2, 51, 3)  # numpy.arange(start, stop, step)

print(my_array) # printing of an array created by arange function

#or


print(np.arange(2, 51, 3))

# Output :

# [ 2  5  8 11 14 17 20 23 26 29 32 35 38 41 44 47 50]

# Process finished with exit code 0


# In[3]:


# Questions 2:
# Accept two lists of 5 elements each from the user.
# Convert them to numpy arrays. Concatenate these arrays and print it. Also sort these arrays and print it.

import numpy as np

my_list_one = []
my_list_two = []

for i in range(5):
    my_input = int(input())
    my_list_one.append(my_input)

print("List one :",my_list_one)

for i in range(5):
    my_input = int(input())
    my_list_two.append(my_input)

print("List Two", my_list_two)

# conversion of List to Array

my_array_one = np.array(my_list_one)
my_array_two = np.array(my_list_two)
print("List to array convert 1 :", my_array_one)
print("List to array convert 2 :", my_array_two)

# concatenation of arrays

array_concat = np.concatenate((my_array_one, my_array_two))

print("concatenation of arrays are :", array_concat)

# Sorting of array

print("Sorted array :", np.sort(array_concat))


#
# Output :
# 1
# 5
# 8
# 9
# 6
# List one : [1, 5, 8, 9, 6]
# 2
# 4
# 8
# 7
# 6
# List Two [2, 4, 8, 7, 6]
# List to array convert 1 : [1 5 8 9 6]
# List to array convert 2 : [2 4 8 7 6]
# concatenation of arrays are : [1 5 8 9 6 2 4 8 7 6]
# Sorted array : [1 2 4 5 6 6 7 8 8 9]

# Process finished with exit code 0


# In[4]:


# Questions 3:
# Write a code snippet to find the dimensions of a ndarray and its size.

import numpy as np

my_array_one = np.array([[1, 4, 7], [3, 6, 9], [1, 4, 7], [3, 6, 9]])
print("calculating Dimensions of a nd array is :", my_array_one.ndim)

print("Size of an array is :", my_array_one.size)

# Output :
# calculating Dimensions of a nd array is : 2
# Size of an array is : 12
#
# Process finished with exit code 0


# In[5]:


# Questions 4:
# How to convert a 1D array into a 2D array? Demonstrate with the help of a code snippet
# Hint: np.newaxis, np.expand_dims

import numpy as np

arr = np.arange(int(input()))
print("Test 1D array (shape) :", arr.shape)

two_d_array_row = arr[np.newaxis]
print("Test` 2D array for row is :", two_d_array_row.shape)

two_d_array_col = arr[:, np.newaxis]
print("Test` 2D array for column is :", two_d_array_col.shape)
# Output :
# 10
# Test 1D array (shape) : (10,)
# Test` 2D array for row is : (1, 10)
# Test` 2D array for column is : (10, 1)
# 
# Process finished with exit code 0


# In[6]:


# Questions 5:
# Consider two square numpy arrays. Stack them vertically and horizontally.
# Hint: Use vstack(), hstack()

import numpy as np

my_array_one = np.square([1, 4, 5, 8, 79, 6, 3, 5, 7, 5, 9, 6, 4, 5])  # square of numpy array
my_array_two = np.square([4, 5, 8, 6, 9, 7, 4, 5, 6])  # square of numpy array


print(" horizontally stacked :", np.hstack((my_array_one, my_array_two)))

print("vertically stacked : ", np.hstack((my_array_one, my_array_two)))


# Output :
#  horizontally stacked : [   1   16   25   64 6241   36    9   25   49   25   81   36   16   25
#    16   25   64   36   81   49   16   25   36]
# vertically stacked :  [   1   16   25   64 6241   36    9   25   49   25   81   36   16   25
#    16   25   64   36   81   49   16   25   36]

# Process finished with exit code 0


# In[7]:


# Questions 6:
# How to get unique items and counts of unique items?


import numpy as np

arr = np.array([4, 7, 8, 9, 5, 6, 5, 4, 4])

unique, counts = np.unique(arr, return_counts=True)
arr = np.asarray((unique, counts)).T
print(arr)

# Output : /home/yogi/Desktop/Python_Code/venv/bin/python
# /home/yogi/Desktop/Python_Code/Lets_Upgrade_Assignments/Day3/Day3_Que6.py

# [[4 3]
#  [5 2]
#  [6 1]
#  [7 1]
#  [8 1]
#  [9 1]]

# Process finished with exit code 0


# In[ ]:




