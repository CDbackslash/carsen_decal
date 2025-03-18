def add(a,b):
    '''This function adds two numbers a and b and returns the result'''
    return a+b
def subtract(a,b):
    '''This function subtracts two numbers a and b and returns the result'''
    return a-b
def multiply(a,b):
    '''This function multiplies two numbers a and b and returns the result'''
    return a*b
def divide (a,b):
    '''This function divides two numbers a and b and returns the result (quotient)'''
    if b != 0:
        return a/b
    else:
        return "Error: Cannot divide by zero."
