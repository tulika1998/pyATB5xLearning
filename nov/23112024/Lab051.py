def sum_three_num(a, b, c):
    return a+b+c
op = lambda a, b, c: a+b+c
print(op(358,85,75))

my_list = [1, 2, 3]
#indexing
print("element at the index 0 -", my_list[0])
print("element at the index 1 -", my_list[1])
print("element at the index 2 -", my_list[2])

#append() : append object to the end of the list
my_list.append(4)
my_list.append(5)
print(my_list)

# extend() - append a new list
my_list.extend([6, 7, 8])
print(my_list)

#insert
my_list.insert(1, "tulika")
print(my_list)

#remove
my_list.remove("tulika")
print(my_list)

