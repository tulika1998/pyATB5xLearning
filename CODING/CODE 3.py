# write a program  to ask the user which browser he want to run automation.
Browser_name = input("Enter the Browser name")
match Browser_name:
    case "firefox":
        print("Starting Firefox")
    case "chrome":
        print("Executing the Chrome code")
    case "edge":
        print("Executing the Edge code")
    case "safari":
        print("Executing the Safari")
    case _:
        print("Match not found")
