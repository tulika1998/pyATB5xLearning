# find the first no repeating character in string
def first_non_repeating(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None


print(first_non_repeating("swiss"))
print(first_non_repeating("dada"))
print(first_non_repeating("annushrita"))
