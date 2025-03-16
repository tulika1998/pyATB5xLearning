#Use the ternary operator to find the maximum of three numbers entered by the user.
x = float(input("enter a number\n"))
y = float(input("enter a number\n"))
z = float(input("enter a number\n"))
if x>y:
    print("x is greater")
elif y>z:
    print("y is greater")
else:
    print("z is greater")

# Get user input
num = float(input("Enter a number: "))

# Calculate square and cube
square = num ** 2
cube = num ** 3

# Display results
print(f"Square of {num} is {square}")
print(f"Cube of {num} is {cube}")