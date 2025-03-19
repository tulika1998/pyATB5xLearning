student_info1 = {
    "name" : "tulika",
    "age" : 25,
    "role" : "tester",
    "address" : {
        "office address" : "kqamd",
        "home address" : "hbdu"
    }

}
student_info2 = {
    "name" : "raj",
    "age" : 20,
    "role" : "developer",
    "address" : {
        "office address" : "fjkhf",
        "home address" : "hbkjchjdu"
    }

}
student_list = [student_info1, student_info2]
print(student_list)
print(student_list[0])
print(student_list[0]["name"])
print(student_list[0]["age"])
print(student_list[0]["address"])
print(student_list[0]["address"]["office address"])
print(student_list[1])
