# Strings
myName = 'Ivan Georgiev'

print(myName[3:6])
print(myName[::3])
print(myName.upper())
print(myName.split())
print(myName.split('a'))

items = "First item: {}. Second item: {}".format("ball", "controller")
items2 = "First item: {first}. Second item: {second}".format(first = "first item", second = "second item")

print(items)
print(items2)
