#write a program to calculate the odd and even
'''def find_even_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

find_even_odd(17)'''

n = int(input("enter a number\n"))
check_even_odd = lambda num: "even" if num % 2 == 0 else "odd"
#print(check_even_odd(18))
#print(check_even_odd(15))
print(check_even_odd(n))