#Tuples
print("Tuples:")

fruits = ("apple", "pear", "watermelon", "cherry", "strawberry")

print(fruits)
print(len(fruits))

for fruit in fruits:
    print(fruit)

if "cherry" in fruits:
    print("Cherry is in the fruits tuple")

print("===================================")

#Sets

print("Sets:")

myFruits = {"apple", "watermelon", "cherry"}
myFruits.add("pear")
myFruits.update(["strawberry", "orange"])
myFruits.remove("apple")
# myFruits.discard("apple")

print("cherry" in myFruits)
print("strawberry" in myFruits)

for myFruit in myFruits:
    print(myFruit)

myFruits.clear()

print(myFruits)

# del myFruits

# print(myFruits)
