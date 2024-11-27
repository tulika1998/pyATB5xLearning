#remove duplicate from dictionary
my_dict = {"a": 1, "b": 2, "c": 2, "d": 3, "e": 4, "f": 4, "g": 5}
unique_value = set()

result = {}
for key, value in my_dict.items():
    if value not in unique_value:
        result[key] = value
        unique_value.add(value)
print(result)



