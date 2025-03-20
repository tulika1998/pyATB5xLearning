#frequecny of characters in string
string = "automation"
string = input("enter the string eg. automation")
char_count = {}
for char in string:
    char_count[char] = char_count.get(char, 0)+1
print(char_count)

