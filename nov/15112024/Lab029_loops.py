i = 0
while i<=10:
    print(i)
    i = i+1
#----------------------------------------------------

for j in range(0, 10):
    if j == 5:
        print("five")
    else:
        print(j)

fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)