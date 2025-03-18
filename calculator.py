import math_tools as mt
print("Welcome to the simple calculator!")
def simplecalc():
    
    input1 = input("Enter the first number (or 'q' to quit): ")
    if input1 == "q":
        print("Goodbye!")
        exit()
    input1 = float(input1)
    input2 = float(input("Enter the second number: "))
    input3 = input("Enter the operation (add, subtract, multiply, divide): ")

    if input3 == "add":
        print("Result:", mt.add(input1,input2))
    elif input3 == "subtract":
        print("Result:", mt.subtract(input1,input2))
    elif input3 == "multiply":
        print("Result:", mt.multiply(input1,input2))
    elif input3 == "divide":
        print("Result:", mt.divide(input1,input2))
    else:
        print("Invalid operation. Please try again.")

    continue_calculating = input("Do you want to continue calculating? (y/n): ")
    if continue_calculating == "y":
        print("Continuing...")
        simplecalc()
    else:
        print("Goodbye!")
    return    
simplecalc()