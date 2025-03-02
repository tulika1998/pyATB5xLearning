class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "tulikakumari123@gmail.com" and self.password == "Tulika@1234":
            print("Allowed, Login success")
        else:
            print("Login failed")

email = input("enter the email \n")
Password = input("enter the Password \n")

vwo_object = VWOLoginPage(email,Password)
vwo_object.login_confirm()

