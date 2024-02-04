# Write a function called 'calculator'. It should take 3 arguments: two integers and a string.
# The string will be either "+", "-", "*", or "/"
# The function should return the result of the corresponding operation on the two numbers in the order they are provided.
# For example, calculator(5, 3, "-") should return 3 and not -2.
# If the string is not one of the specified operations, the function should print "Invalid Operator".
# Run python3 -m unittest test_functions.py in your terminal to check your work.

def calculator(x, y, operator):
    if operator == "+":
        return x + y
    if operator == "-":
        return x - y
    if operator == "*":
        return x * y
    if operator == "/":
        return x / y
    print("Invalid Operator")
    return
