### Problem 1
#  Oski hacked your computer and you can no longer use x**y or pow(x, y). Find
# a different way (by writing a function) that can compute x raised to the power
# of y.
x = 2
y = 5

def computePower(x, y):
    '''This function takes x and raises it to the power of y'''
    count = x
    for i in range(1, y):
        count = count * x
    result = count
    return result
print("Problem 1 result:")
print(computePower(x, y))



### Problem 2
# You are trying to decide what to wear to the Python DeCal lecture, but you
# are only concerned about the day’s lowest and highest temperatures. Write a
# function that takes in a list as input and returns a tuple with the min and max
# as two values.
readings = [15, 14, 17, 20, 23, 28, 20]
def temperatureRange(readings):
    '''This function takes a list of readings and returns the min and max as a tuple'''
    max_temp = max(readings)
    min_temp = min(readings)
    temp_tuple = (min_temp, max_temp)
    return temp_tuple
print("Problem 2 result:")
print(temperatureRange(readings))

### Problem 3
# All your classes have assigned problem sets due next week, and you want to
# check if it’s the weekend so you have time to work on them. Write a function
# that takes a day of the week (represented as an integer, where 1 = Monday, 2
# = Tuesday, etc) and returns True if its a weekend and False if otherwise.
day = 6 # Saturday
def isWeekend(day):
    '''This function takes a day of the week and returns True if its a weekend (6 or 7) and False if otherwise'''
    if day == 6 or day == 7:
        return True
    else:
        return False
print("Problem 3 result:")
print(isWeekend(day))


### Problem 4
# The Python DeCal wants to take a trip to the Lick Observatory ( San Jose,
# CA) and they want to pick the best car. Write a function that takes the distance
# traveled (in miles) and the amount of fuel consumed (in gallons) as input and
# returns the fuel efficiency.
distance = 70 # miles
fuel = 21.5 # gallons
def fuel_efficiency(distance, fuel):
    efficiency = distance / fuel
    return efficiency
print("Problem 4 result:")
print(fuel_efficiency(distance, fuel))


### Problem 5
# Write a function that takes an integer as input and moves its last digit to the
# front of the number. You may NOT convert the input to a string. Hint: Try
# modulus (%) and floor division. (\\) to solve this problem.
n = 12345
def decodeNumbers(n):
    '''This function takes an integer and moves its last digit to the front of the number'''
    last_digit = n % 10  
    number_size = n
    i = 0
    while number_size != 1:
        number_size = number_size // 10
        i = i + 1
    new_number = ( (n - last_digit) // 10) + last_digit * (10**i) # subtracts the last digit, then adds it to the front
    return new_number
print("Problem 5 result:")
print(decodeNumbers(n))


### Problem 6
# Oh no! Oski hacked you computer again... now you have lost the ability to use
# min() and max(). Write two functions to manually find the minimum and 
# maximum values in a list of numbers with for loops.
nums = [2024, 98, 131, 2, 3, 72]
def find_min_with_for_loop(nums):
    '''This function assumes the first number is the minimum, then checks if any other number is smaller. If it is, that number is assigned as the new minimum'''
    min_value = nums[0]
    for i in nums:
        if i < min_value:
            min_value = i
    return min_value
print("Problem 6 result:")
print("Min:", find_min_with_for_loop(nums))

def find_max_with_for_loops(nums):
    max_value = nums[0]
    for i in nums:
        if i > max_value:
            max_value = i
    return max_value
print("Max:", find_max_with_for_loops(nums))

# Write two functions to manually find the minimum and maximum values in a
# list of numbers with while loops.
nums = [2024, 98, 131, 2, 3, 72]
def find_min_with_while_loop(nums):
    min_value = nums[0]
    i = 0
    while  i < len(nums):
        if nums[i] < min_value:
            min_value = nums[i]
        i = i + 1
    return min_value
print("Min:", find_min_with_while_loop(nums))


def find_max_with_while_loops(nums):
    max_value = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] > max_value:
            max_value = nums[i]
        i = i + 1
    return max_value
print("Max:", find_max_with_while_loops(nums))

### Problem 7
# Write a function that takes a string as an input and returns the number of vowels
# in the string and the number of consonants in the string as tuple. Don’t forget
# about capital letters! Hint: You can use .isalpha() to check if a character is
# a letter.
text = "UC Berkeley, founded in 1868!"
def vowel_and_consonant_count(text):
    '''This function takes a string and returns the number of vowels and consonants as a tuple'''
    consonant_count = 0
    vowel_count = 0
    for i in range(len(text)):
        letter = text[i]
        if letter.isalpha():
            # Would it be possible to do this part as a dictionary? I'm not sure how
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
                vowel_count = vowel_count + 1
            else:
                consonant_count = consonant_count + 1
    return (vowel_count, consonant_count)
print("Problem 7 result:")
print(vowel_and_consonant_count(text))


### Problem 8
# Write a function that takes an integer as an input and returns the sum of its
# digits.
num = 24689
def digital_root(num):
    '''This function takes an integer and returns the sum of its digits, by first converting to a string, then reconverting each entry in the string back to an integer while adding them'''
    new_num = 0
    string_num = str(num)
    for i in string_num:
        new_num = new_num + int(i)
    return (new_num)
print("Problem 8 result:")
print(digital_root(num))