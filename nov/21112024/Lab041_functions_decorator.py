def add_security(func):

    def wrapper():
        print("1. before the function is called")
        print("2. wear helmet, tight belt")
        func()
        print("3.after the function is called")
        print("4.secure driving, leave all the items")

    return wrapper()

@add_security
def drive_ola_scooty():
    print("ola")


@add_security
def driving_scooty():
    print("normal function !")
    print("I am driving scooty !")


