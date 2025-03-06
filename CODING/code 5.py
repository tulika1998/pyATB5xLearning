'''Take a input from a user and print the table


n = 2 & print
2 x 2 = 4
2 x 4 = 8
2 x 6 = 12
2 x 8 = 16
2 x 10 = 20
'''
N = int(input("Enter the number"))
for i in range(2, 21, 2):
    print(f"{N} x {i} = {N * i}")
