# Functions
def print_hello():
    print("hello")

print_hello()

def print_info(name, country = "Bulgaria"):
    # print("My name is " + name + " and I am from " + country)
    print("My name is {} and I am from {}".format(name,country))

print_info("Ivan") # print_info("Ivan", "Croatia")

def return_hello():
    return "hello"

result = return_hello()

print(result)
print(type(result))

print("======================")

# Filter

myNumbers = [3, 6, 13, 21, 42]

def check_odd(num):
    return num%2 != 0

oddNumbers = filter(check_odd, myNumbers)

print(list(oddNumbers))

print("======================")

# Lambda function

result2 = lambda x, y, z : x * y * z

print(result2(1,2,3))

oddNumbers2 = filter(lambda num : num%2 != 0, myNumbers)

print (list(oddNumbers2))
