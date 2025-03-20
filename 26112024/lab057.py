dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1, "b": 2}
missing_keys = set(dict1.keys()) - set(dict2.keys())
print(missing_keys)

# Sort a dictionary by its values in descending order
my_dict = {"a": 3, "b": 1, "c": 2}

# {b: 1 , c: 2 , a :3}

# Sort a dictionary by its values in descending order.
sorted_dict = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
print(sorted_dict)


# function that returns the maximum value from the dictionary
def max_value_dict(dictionary):
    return max(dictionary.values())


print(max_value_dict({"a": 30, "b": 40, "c": 20}))
