class person:
    def __init__(self):
        print("I will be called")
        self.name = input("enter my name\n")
        self.age = input("enter my age\n")
        self.address = input("enter my address\n")
        self.occupation = input("enter my occupation\n")

    def name_of_function_to_be_displayed(self):
        print(f"Name is {self.name}", f"Age is {self.age}", f"address is{self.address}", f"occupation is {self.occupation}")

person1 = person()
person1.name_of_function_to_be_displayed()