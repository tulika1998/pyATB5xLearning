#Create a program that checks whether a given string is a palindrome. A palindrome is a word or phrase
# that reads the same backward as forward (ignoring spaces, punctuation, and capitalization). Use an
# if-else statement to determine if the string is a palindrome.
import re

def is_palindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned_str == cleaned_str[::-1]

# Taking input from the user
input_string = input("Enter a string: ")

# Checking if the string is a palindrome
if is_palindrome(input_string):
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
