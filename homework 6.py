import numpy as np


# # # # # Problem 1 # # # # #
# You have obtained a dataset of star temperatures from different stellar clusters.
# For your research, you are interested only in clusters where at least one star’s
# temperature is a prime number. Given a 2D NumPy array, write a function to
# find the rows where at least one value is a prime number. For example:

arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
def containsPrimes(arr):
    primesarray = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] % 2 != 0 and arr[i][j] % 3 != 0 and arr[i][j] % 5 != 0 and arr[i][j] % 7 != 0 or arr[i][j] == 2 or arr[i][j] == 3 or arr[i][j] == 5 or arr[i][j] == 7:
                primesarray.append(arr[i])
                break
    return primesarray
print("Problem 1 Result:")
print(containsPrimes(arr))
# This function only works for prime numbers up to 81. To work for larger prime numbers, we need a more lgorithm to check for them.

#################### How do i make this give one big array insteada of 3 small arrays? ####################


# # # # # Problem 2 # # # # #
# You’ve decided to take a break from your cutting-edge research and play checkers
# with your friend. Unfortunately, there is no checkerboard in sight! Therefore
# you must create one yourself.

# Start by writing a function that creates a 8x8 square matrix with only zeros.
def checkerboard():
    array = np.zeros((8,8))
    return array
print("Problem 2.1 Result:")
print(checkerboard())
# array([[0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0]] )



# For only the odd rows, make an alternating pattern of ones and zeroes.
def checkerboard():
    array = np.zeros((8,8))
    for i in range(len(array)):
        if i % 2 == 0:
            for j in range(len(array[i])):
                if (j) % 2 == 0:
                    array[i][j] = 1
    return array
print("Problem 2.2 Result:")
print(checkerboard())    
# array([[1, 0, 1, 0, 1, 0, 1, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [1, 0, 1, 0, 1, 0, 1, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [1, 0, 1, 0, 1, 0, 1, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [1, 0, 1, 0, 1, 0, 1, 0],
# [0, 0, 0, 0, 0, 0, 0, 0]] )


# Finish the checkerboard with the even rows.
def checkerboard():
    array = np.zeros((8,8))
    for i in range(len(array)):
        if i % 2 == 0:
            for j in range(len(array[i])):
                if (j) % 2 == 0:
                    array[i][j] = 1
        if i % 2 != 0:
            for j in range(len(array[i])):
                if (j+1) % 2 == 0:
                    array[i][j] = 1
    return array
print("Problem 2.3 Result:")
print(checkerboard())    
# array([[1, 0, 1, 0, 1, 0, 1, 0],
# [0, 1, 0, 1, 0, 1, 0, 1],
# [1, 0, 1, 0, 1, 0, 1, 0],
# [0, 1, 0, 1, 0, 1, 0, 1],
# [1, 0, 1, 0, 1, 0, 1, 0],
# [0, 1, 0, 1, 0, 1, 0, 1],
# [1, 0, 1, 0, 1, 0, 1, 0],
# [0, 1, 0, 1, 0, 1, 0, 1]] )


# Re-write your function such that the checkerboard begins with a 0 instead.
def reverse_checkerboard():
    array = np.zeros((8,8))
    for i in range(len(array)):
        if i % 2 == 0:
            for j in range(len(array[i])):
                if (j+1) % 2 == 0:
                    array[i][j] = 1
        if i % 2 != 0:
            for j in range(len(array[i])):
                if (j) % 2 == 0:
                    array[i][j] = 1
    return array
print("Problem 2.4 Result:")
print(reverse_checkerboard())   
# array([[0, 1, 0, 1, 0, 1, 0, 1],
# [1, 0, 1, 0, 1, 0, 1, 0],
# [0, 1, 0, 1, 0, 1, 0, 1],
# [1, 0, 1, 0, 1, 0, 1, 0],
# [0, 1, 0, 1, 0, 1, 0, 1],
# [1, 0, 1, 0, 1, 0, 1, 0],
# [0, 1, 0, 1, 0, 1, 0, 1],
# [1, 0, 1, 0, 1, 0, 1, 0]] )




# # # # # Problem 3 # # # # #
# You have now become fascinated with how dark energy is making galaxies ac-
# celerate away from us. Write a function that takes in a string and a number,
# and returns the string with the specified number of spaces inserted between each
# letter, simulating the expansion of space! For example:
universe = np.array(['galaxy', 'clusters'])
def expansion(input_array, spaces):
    new_array = []
    for i in range(len(input_array)):
        new_string = ""
        for j in range(len(input_array[i])):
            new_string = new_string + input_array[i][j]
            new_string = new_string + (" " * spaces)
        new_array.append(new_string.strip())
    return new_array
print("Problem 3 Result:")
print(expansion(universe, 2))
# array([‘g a l a x y’, ‘c l u s t e r s’])
# >>> expansion(universe, 2)
# array([‘g a l a x y’, ‘c l u s t e r s’])


# # # # # Problem 4 # # # # #
# While analyzing a dataset of star luminosities, you need to identify the second-
# dimmest star in each cluster. Write a function that takes a 2D NumPy array
# and returns an array containing only the second-smallest value in each column.
# For example:
np.random.seed(123)
stars = np.random.randint(500, 2000, (5, 5))
# array([[1123, 1456, 1789, 1324, 1876],
# [1567, 1987, 1678, 1405, 1589],
# [1345, 1654, 1523, 1109, 1923],
# [1298, 1890, 1367, 1784, 1432],
# [1823, 1756, 1489, 1672, 1550]])
def secondDimmestColumn(stars):
    columnArray = np.transpose(stars)
    sortedColumn = []
    secondDimmest = []
    for i in range(len(columnArray)):
        sortedColumn = np.sort(columnArray[i])
        secondDimmest.append(sortedColumn[1])
    return np.array(secondDimmest)
print("Problem 4 Result:")
print("The star array is:")
print(stars)
print("The second dimmest stars in each column are:")
print(secondDimmestColumn(stars))
    
# >>> secondDimmest(stars)
# array([1298, 1654, 1489, 1324, 1550])