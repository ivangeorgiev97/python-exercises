# Functions
def print_hello():
    print("hello")

print_hello()

def print_info(name, country = "Bulgaria"):
    # print("My name is " + name + " and I am from " + country)
    print("My name is {} and I am from {}".format(name,country))

print_info("Ivan") # print_info("Ivan", "AnotherCountry")

def return_hello():
    return "hello"

result = return_hello()

print(result)
print(type(result))

print("======================")

# Filter

my_numbers = [3, 6, 13, 21, 42]

def check_odd(num):
    return num%2 != 0

odd_numbers = filter(check_odd, my_numbers)

print(list(odd_numbers))

print("======================")

# Lambda function

result2 = lambda x, y, z : x * y * z

print(result2(1,2,3))

odd_numbers2 = filter(lambda num : num%2 != 0, my_numbers)

print (list(odd_numbers2))
