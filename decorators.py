def my_function(name="Ivan"):

    print("test")

    def print_hello():
        return "hello"

    def print_bye():
        return "bye"

    if name == "Ivan":
        return print_hello
    else:
        return print_bye

testFunction = my_function()

print(testFunction())

print("====================")

def print_hi():
    return "hi"

def another_function(func):
    print("hello")
    print(func())

another_function(print_hi)

print("====================")

def test_decorator(func):

    def test():
        print("test")
        func()
        print("test1")

    return test

@test_decorator
def test2():
    print("test2")

# test2 = test_decorator(test2)

test2()
