a = 10  # 1010 in binary
b = 4   # 0100 in binary
print(a | b)

def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")

person = {"name": "Alice", "age": 25}
greet(**person)