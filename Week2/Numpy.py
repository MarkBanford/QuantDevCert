import numpy as np

# Create a large NumPy array (eg. 1 million random floats from uniform distribution)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# large = np.random.uniform(0, 100, size=100)

large = np.asarray(list)

# Grab the first 100 elements

# print(large)

first_five = large[0:5]

# # Grab the last 100 elements
#
last_five = large[-5:]
#
# # Add both of these and print the output
#
added = first_five + last_five

# Create a large randomised matrix (eg. 100 x 100)
np.random.seed(0)  # makes sure we get the same matrix each run
large_rand = np.random.randint(0, 100, size=10_000).reshape(100, 100)

# Do basic operations on the matrix, like multiplication and addition and print the output

mmult = large_rand * 3

# Create a matrix of ones and then zeros

a = np.zeros((10, 10), int)
np.fill_diagonal(a, 1)

print(a)
