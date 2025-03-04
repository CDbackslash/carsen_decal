##### Homework 1/2 Review #####

# In your .py file, please answer these questions as comments. Pretend your
# name is Judy.

# 1. You have been plopped into this directory system. What command will
# tell you what your working directory is?
# - pwd

# 2. The command tells you ∼/python decal/judy decal. What command
# with list all the files in your current working directory?
# - ls

# 3. Brianna just sent out an announcement that there was a typo on homework.py.
# So you need to pull the updates. What commands will let you move to
# the correct repository and pull the latest changes?
# - cd ../brianna_repo
# - git pull

# 4. How would you move this new homework.py to your personal repository
# homework directory?
# - mv homework.py ../judy decal/homework

# 5. You want to see the contents of the homework.py in your terminal from
# your personal repository. What command(s) will let you do this?
# - cat homework/homework.py     

# 6. You want to edit the contents of the homework.py in your terminal from
# your personal repository. What command will let you do this?
# - nano homework/homework.py

# 7. You have finished the homework. What commands will allow you to save
# the changes and push from your local repository to your remote repository?
# - git add homework.py
# - git commit -m "Uploading homework 5"
# - git push origin master

# 8. Oh no! Git gave you the following error. What commands should you call
# to resolve this error and push your homework properly? What does the
# error mean? (i.e. what did ”Judy” do wrong?)
# - Pushing work to the remote repository from another computer would desync
# - the local and remote repositories for one machine, which could be what Judy
# - did wrong. To fix this, Judy should simply use git pull to update her local
# - repository, then git push to upload her new changes. 

# 9. What absolute path will allow you to move to Recents/?
# - cd ~/Recents

##### Homework 3 Review #####

# Write a function that takes any input and returns a string indicating its data
# type.
def checkDataType(input):
    return str(type(input)).split("'")[1]
print("Problem 1 Result:")
print(checkDataType(3.14))
print(checkDataType(True))

# Write a function that takes an integer as input and returns ’Even’ if the integer
# is even, and ’Odd’ otherwise.
def checkEvenOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print("Problem 2 Result:")
print(checkEvenOdd(7))
print(checkEvenOdd(10))

# Write a function that takes a list of integers and returns their sum using a loop
# (do NOT use the built-in sum() function).
numbers = [1, 2, 3, 4, 5]
def sumWithLoop(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + numbers[i]
    return sum
print("Problem 3 Result:")
print(sumWithLoop(numbers))

##### Homework 4 Review #####

# Write a function that takes a list and returns a new list with each element
# duplicated.
# >>> duplicateList([‘a’, ‘b’, ‘c’])
# [‘a’, ‘a’, ‘b’, ‘b’, ‘c’, ‘c’]
list = ['a', 'b', 'c']
def duplicateList(list):
    new_list = []
    for i in range(len(list)):
        new_list.append(list[i])
        new_list.append(list[i])
    return new_list
print("Problem 4 Result:")
print(duplicateList(list)) 

#  There’s an error in the following function that’s supposed to return the square
# of a number. Find and correct it:
def square(num):
    return num * num
print("Problem 5 Result:")
print(square(5))

##### Homework 2 Review #####

# Please take a screenshot of you adding, committing and pushing this home-
# work from your local to your remote repository. Include this screenshot in your
# Gradescope submission!