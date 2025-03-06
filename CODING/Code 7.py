'''✅ Pyramid pattern in Java

    *
   ***
  *****
 *******
*********
'''

row = 5
for i in range(1, row + 1, 1):
    print(" " * (row - i), end="")
    # Print stars
    print("*" * (2 * i - 1))
