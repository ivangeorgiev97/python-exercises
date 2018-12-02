# Classes and Objects

class MainClass:
    hobby = "football"

    def introduce_me():
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
      print("object is removed!")

  def introduce_me(self):
    print("My name is " + self.name + " and I am from " + self.country + " my hobby is " + MyClass.hobby)

myObject = MyClass("Ivan", "Bulgaria")

myObject.introduce_me()

myObject.name = "Stoyan"
myObject.introduce_me()

print(myObject)
