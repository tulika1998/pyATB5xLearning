'''Print  lines of output; each line  (where ) contains the  of  in the form:
N x i = result.
Sample Input
2


Sample Output


2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20'''

N = int(input("Enter a number: "))  # Taking input from the user

for i in range(1, 11):  # Loop from 1 to 10
    print(f"{N} x {i} = {N * i}")
