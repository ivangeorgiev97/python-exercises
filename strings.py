# Strings
my_name = 'Ivan Georgiev'

my_name_it = iter(my_name)

print(next(my_name_it))
print(my_name[3:6])
print(my_name[::3])
print(my_name.upper())
print(my_name.split())
print(my_name.split('a'))

items = "First item: {}. Second item: {}".format("ball", "controller")
items2 = "First item: {first}. Second item: {second}".format(first = "first item", second = "second item")

print(items)
print(items2)
