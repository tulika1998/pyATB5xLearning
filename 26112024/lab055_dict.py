#dictionary from two list
key = ["name", "role", "experience"]
value = ["tulika", "tester", 3]

my_dict = dict(zip(key,value))
print(my_dict)

#merge two dictionary
dict1 = {"a" : 1, "b" : 2}
dict2 = {"c" : 3, "d" : 4}
merged_dict = dict1 | dict2
print(merged_dict)
print(merged_dict.get("a"))