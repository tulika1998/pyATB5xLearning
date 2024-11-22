num1 = int(input("enter the num1\n"))
num2 = int(input("enter the num2\n"))
num3 = int(input("enter the num3\n"))

def sum_of_three(n1=100, n2=200, n3=300):
    return n1 + n2 + n3

result= sum_of_three(num1 , num2, num3)
print(result)

result2 = sum_of_three()
print(result2)


