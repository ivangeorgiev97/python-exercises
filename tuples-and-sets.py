#Tuples
print("Tuples:")

fruits = ("apple", "pear", "watermelon", "cherry", "strawberry")

print(fruits)
print(len(fruits))

my_new_it = iter(fruits)
print(next(my_new_it))


for fruit in fruits:
    print(fruit)

if "cherry" in fruits:
    print("Cherry is in the fruits tuple")

print("===================================")

#Sets

print("Sets:")

my_fruits = {"apple", "watermelon", "cherry"}
my_fruits.add("pear")
my_fruits.update(["strawberry", "orange"])
my_fruits.remove("apple")
# my_fruits.discard("apple")

print("cherry" in my_fruits)
print("strawberry" in my_fruits)

for my_fruit in my_fruits:
    print(my_fruit)

my_fruits.clear()

print(my_fruits)

# del my_fruits

# print(my_fruits)
