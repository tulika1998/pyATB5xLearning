#web automation -selenium
from dotenv import load_dotenv
import os
class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "tulikakumari123@gmail.com" and self.password == "Tulika@1234":
            print("Allowed, Login success")
        else:
            print("Login failed")
load_dotenv()
email = os.getenv("email")
Password = os.getenv("password")
print(email, Password)

vwo_object = VWOLoginPage(email,Password)
vwo_object.login_confirm()
