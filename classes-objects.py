# Classes and Objects

class MainClass:
    hobby = "football"

    def introduce_me(self):
        "Hi, my name is Ivan"


class MyClass(MainClass):
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return "Name: {}, Country: {}, Hobby: {}".format(self.name, self.country, MyClass.hobby)

    def __len__(self):
        return self.name

    def __del__(self):
        print("object is finally removed!")

    def introduce_me(self):
        print(f'My name is {self.name} and I am from {self.country} and hey my hobby is {MyClass.hobby}')


myObject = MyClass("Ivan", "Bulgaria")

myObject.introduce_me()

myObject.name = "Stoyan"
myObject.introduce_me()

print(myObject)

class Animal:
    def __init__(objhere, name):
        objhere.name = name

    def say_name(againreferncehere):
        print ("Hey " + againreferncehere.name)

a3 = Animal("Onqotnovagodina")
a3.say_name()
