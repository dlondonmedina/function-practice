# Create a function called capitalize that takes a string as an input
# The input string will be a sequence of words separated by spaces
# The function should return the input string with the first letter of each word capitalized
# For example, capitalize("hello world") should return "Hello World"
# If the first letter of a word is already capitalized, the function should leave that word unchanged
# Run python3 -m unittest test_grammar.py in your terminal to check your work.

def capitalize(text):
    new = ""
    previous=None
    for letter in text:
        if previous is None or previous == " ":
            new = new + letter.upper()
        else:
            new = new + letter
        previous = letter

    return new
