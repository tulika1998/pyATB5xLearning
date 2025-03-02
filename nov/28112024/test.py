def rearrange_even_numbers(array):
    evens =[num for num in array if num % 2 == 0]
    result = []
    even_index = 0
    for num in array:
        if num % 2 == 0:

result.append(evens[even_index])
    even_index +=1
    else:

input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output_array = rearrange_even_numbers(input_array)
print("original array:" input_array)
print("rearranged array:" ouput_array)