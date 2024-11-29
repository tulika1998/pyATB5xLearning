'''Task 1 - Create a Class PyATB , 5 Attributes, 3 Functions/Methods
Use PC - to set the value of the attributes
create a Print student information method/function
3 studetns objects
PyATB().print_student_infomation()'''

class PyATB:
    name = None
    age = None
    gender = None
    occupation = None
    address = None
    phone_number = None

    def __init__(self, name, age, gender, occupation, address, phone_number):
     self.name = name
     self.age = age
     self.gender = gender
     self.occupation = occupation
     self.address = address
     self.phone_number = phone_number

    def print_student_info(self):
         print(f"Name is {self.name}", f"Age is {self.age}", f"Gender is {self.gender}", f"Occupation is {self.occupation}",
         f"Address is {self.address}", f"Phone_number is {self.phone_number}")

Student1 = PyATB("Rahul", "23", "Male", "Tester", "ASD",
                 "98789877678")
Student2 = PyATB("Rita", "29", "Female", "Manual Tester",
                 "JFHN", "987545477678")
Student3 = PyATB("Ram", "21", "male", "Automation Tester",
                 "JfhfN", "98754599978")

Student1.print_student_info()
Student2.print_student_info()
Student3.print_student_info()