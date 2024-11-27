#write a program to count the frequency of each string
string = "Automation"
string + input("Enter the input e.g. automation")
char_count = {}
for char in string:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)