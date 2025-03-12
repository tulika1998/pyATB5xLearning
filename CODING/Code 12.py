#how to remove punctuation  from string in python
import string

test_str = 'learning, Automation: for ! RD;'
test_str = (test_str.translate
            (str.maketrans('', '', string.punctuation)))
print(test_str)

try:
    # Ask the user to input a number
    user_input = input("Please enter a number: ")

    # Try to convert the input into an integer
    number = int(user_input)

    # If successful, print the number
    print("You entered the number:", number)

except ValueError:
    # If there's a ValueError (e.g., if the input isn't a number), handle it here
    print("Oops! That was not a valid number. Please try again.")


'''try block: This is where you write the code that might cause an error. In this case, trying to convert the
 user's input into an integer.
except block: If an error occurs inside the try block (for example, if the user enters something 
that cannot be converted to an integer), the program will jump to this except block and handle the error
 gracefully without crashing.'''