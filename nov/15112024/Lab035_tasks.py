#✅ FizzBuzz Test:

#Write a program that prints numbers from 1 to 100. However, for multiples of 3, print "Fizz" instead of the
#number, and for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz.
# " ( for, if)

for number in range(1, 100):
    if number % 3 ==0 and number % 5 ==0:
        print("fizzbuzz")
    elif number % 5 ==0:
        print("buzz")
    elif number % 3 ==0:
        print("fizz")
    else:
        print(number)