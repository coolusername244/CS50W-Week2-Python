def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Function finished")
    return wrapper

@announce
def hello():
    print("Hello, World!")  

hello()