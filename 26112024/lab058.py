my_dict = {'a': 2, 'e': 5, 'd': 1, 'c': 7, 'b': 3}
print(my_dict)

sort_dict= sorted(my_dict.items())
sort_dict1= sorted(my_dict.keys())
sort_dict2= sorted(my_dict.values(),reverse=True)
sort_dict3= sorted(my_dict.values(),reverse=False)
print((sort_dict))
print((sort_dict1))
print((sort_dict2))
print((sort_dict3))

'''Question 2 : 
my_list = [1, 2, 2, 3, 4, 4, 5]
Remove duplicates from a list using a set.
Output: [1, 2, 3, 4, 5]'''
my_list = set([1, 2, 2, 3, 4, 4, 5])
print(my_list)
