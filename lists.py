# Lists
myNumbers = [21, 3, 18, 15, 6]
myNumbers.sort()

print(myNumbers)

myNumbers2 = [13, 6 ,42]
myNumbers2.reverse()

print(myNumbers2)

me = ['Ivan', 21, 6, True, 'Georgiev', [6,3,13]]

print(len(me))
print(me[-1])

me[2] = 'IvanGeorgiev'
me.append('hello')
me2 = ['a', 'b', 'v']
me.extend(me2)

print(me)
print(me.pop())
print(me.pop(-1))
