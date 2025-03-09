#user defined
#1.they cannot return
#no return and no parameter/no argument

def greet():
    print("hello")

greet()

#2. they can return something
#no return type and argument type
def greet_by_name(name):
    print("hello,",name)

greet_by_name("tulika")

#3.no return type and with default argument
def say_hello_default_arg(name="tulika"):
    print("hello", name.upper())

say_hello_default_arg("kumari")
say_hello_default_arg()

#multiple arguments
def multiple_arg(name1 = "A", name2 = "B"):
    print("Mul -> ", name1, name2)

multiple_arg()
multiple_arg(name1="tulika")
multiple_arg(name1 = "rekha", name2 = "devi")

#4.argument and return type
def sum_of_two(a, b):
    return a+b
result= sum_of_two(a=43,b=67)
print(result)

