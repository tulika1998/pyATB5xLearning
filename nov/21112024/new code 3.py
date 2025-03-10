import time
def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("total time taken by func -> ", end_time-start_time)
    return wrapper()

@time_decorator
def test_ui1():
    print("add the function, time taken by this function 1")
    time.sleep(2)

@time_decorator
def test_ui2():
    print("add the function, time taken by this function 2")
    time.sleep(5)

