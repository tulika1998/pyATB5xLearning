#Count vowels and consonants in a String
input_string = "Hello world"
vowels = "aeiou"
vowels_count = 0
consonants_count = 0
result = dict()
for char in input_string:
    if char in vowels:
        vowels_count = vowels_count + 1
    else:
        consonants_count = consonants_count + 1
print(vowels_count)
print(consonants_count)