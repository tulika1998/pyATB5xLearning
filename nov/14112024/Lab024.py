num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))
num3 = int(input("Enter the num3\n"))
if num1>num2 and num1>num3:
    print("max is", num1)
elif num2>num1 and num2>num3:
    print("max is", num2)
else:
    print("max is", num3)