def classify_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalne"
    else:
        print("not a valid length")

side1 = float(input("Enter the side1\n"))
side2 = float(input("Enter the side2\n"))
side3 = float(input("Enter the side3\n"))

result = classify_triangle(side1, side2, side3)
print(f"the result is: {result}"
