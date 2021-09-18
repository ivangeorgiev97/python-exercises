# Lists
my_numbers = [21, 3, 18, 15, 6]
my_numbers.sort()

print(my_numbers)

my_numbers2 = [13, 6 ,42]
my_numbers2.reverse()

print(my_numbers2)

me = ['Ivan', 24, 6, True, 'Georgiev', [6,3,13]]

print(len(me))
print(me[-1])

me[2] = 'IvanGeorgiev'
me.append('hello')
me.insert(1, 'hey')
me2 = ['a', 'b', 'v']
me.extend(me2)

new_list = [x for x in me2 if "v" in x]

print(me)
print(me.pop())
print(me.pop(-1))
print(new_list)
