score = int(input("enter the score\n"))
if score >=90 and score <= 100:
    print("you grade is", "A")
elif score >=80 and score <= 89:
    print("you grade is", "B")
elif score >=70 and score <= 79:
    print("you grade is", "C")
elif score >= 60 and score <= 69:
    print("you grade is", "D")
elif score >=100:
    print("you are a superman!, you cannot get a grade")
else:
    print("your grade is", "F")



