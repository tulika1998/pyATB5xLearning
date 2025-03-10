def add_before_ui_after_ui(func):

    def wrapper():
        print("Before the running UI TC")
        print("Start the browser")
        func()
        print("Ending the running UI TC")
        print("Quit the browser")
    return wrapper()


@add_before_ui_after_ui
def test_ui():
    print(">>I will test the UI")

