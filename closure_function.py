def outer_func():
    def inner_func():
        print("inside the inner function")
    
    return inner_func

varF = outer_func()
varF()

def out_func(name):
    def in_func():
        print(f"Hello {name}, Welcome to Python Programming language!!")

    return in_func

user = out_func("Omkar")
user()