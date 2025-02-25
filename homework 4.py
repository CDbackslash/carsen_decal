# As you work through this problem set, whenever you encounter an error, please
# include a comment explaining what the error was and how you later resolved it.
# You can add these explanations at any relevant place in the file. Example:
# >>> print("Hello, World!")
# >>> """
# >>> I encountered the following eror: "SyntaxError: unterminated
# >>> string literal (detected at line 1) when I wrote
# >>> print("Hello, World!)". So I added the missing " at the end
# >>> and the code printed it successfully.
# >>> """


# # Problem 1
# Create a variable (name it anything you want, but make it descriptive!) that
# is assigned to a list with numbers 0 through 20. You should not write each
# number manually.
num_list = []
i = 0
while i <= 20:
    num_list.append(i)
    i = i + 1
print("Problem 1 result:")
print(num_list)
# I originally had i < 20, but I realized that the list was not including 20.
# I fixed this by changing the condition to i <= 20.


# # Problem 2
# Write a function that will take in your list from Problem 1 and square each element
# in the list. Assign the result to a new variable.
def squareList(num_list):
    squared_num_list = num_list.copy()
    for i in range(len(num_list)):
        squared_num_list[i] = num_list[i] ** 2
    return squared_num_list
squared_num_list = squareList(num_list)
print("Problem 2 result:")
print(squared_num_list)

# This function used to accidentally change the value of num_list. I fixed this by
# using .copy() to create a new list that is a copy of num_list, so they are separate.

# # Problem 3
# Write a function that takes in your new list from Problem 2 and returns the first
# 15 elements of the list using slicing.

def first_fifteen_elements(num_list):
    return num_list[:15]
print("Problem 3 result:")
print(first_fifteen_elements(squared_num_list))



# # Problem 4
# Write a function that takes in your list from Problem 2 and returns every 5th
# element from the list using striding.
def every_fifth_element(num_list):
    return num_list[::5]
print("Problem 4 result:")
print(every_fifth_element(num_list))



# # Problem 5
# Write a function that takes your list from Problem 2, slices the last 3 elements of
# the list, and then returns every 3rd element from that list in reverse order.
def fancy_function(num_list):
    list_size = len(num_list) - 4
    fancy_list = num_list[list_size::-1]
    return fancy_list[::3]
print("Problem 5 result:")
print(fancy_function(squared_num_list))


# # Problem 6
# Write a function that uses nested for loops to create a 5x5 2D list where the
# numbers 1 through 25 are stored sequentially. Assign the result to a new vari-
# able.
def create_2d_list():
    matrix = []
    sub_matrix = []
    running_total = 0
    for i in range(6):
        if i != 0:
            matrix.append(sub_matrix)
            sub_matrix = []
        for j in range(5):
            sub_matrix.append(j+1+5*i)
    return matrix
matrix = create_2d_list()
print("Problem 6 result:")
print(matrix)
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
[16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]


# # Problem 7
# With the 2D list you created in Part 3.1, write a function that will replace all
# multiples of 3 with the character “?”.
def modify_2d_list(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = "?"
    return matrix
print("Problem 7 result:")
print(modify_2d_list(matrix))
modified_matrix = matrix
# [[1, 2, ‘?’, 4, 5],
# [‘?’, 7, 8, ‘?’, 10],
# [11, ‘?’, 13, 14, ‘?’],
# [16, 17, ‘?’, 19, 20],
# [‘?’, 22, 23, ‘?’, 25]]


# # Problem 8
# Assign the result of your function from Problem 7 to a variable. Write a function
# that will iterate through the new 2D list variable and return the sum of all the
# elements that are not “?”. Hint: Try using “!=”.
def sum_2d_list(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "?":
                sum = sum + matrix[i][j]
    return sum
print("Problem 8 result:")
print(sum_2d_list(modified_matrix))
217