# list comprehension

# my_list = [x for x in "program"]
# # my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
# print("my_list[5: ] =", my_list[5: ])
# print("my_list[:-4] =", my_list[:-4])
# print("my_list[:] =", my_list[:])
# print("my_list[::2] =", my_list[::2])

# # my_list[5: ] = ['a', 'm']
# # my_list[:-4] = ['p', 'r', 'o']
# # my_list[:] = ['p', 'r', 'o', 'g', 'r', 'a', 'm']     
# # my_list[::2] = ['p', 'o', 'r', 'm'] --> [start: stop: step]

fruits = ['apple', 'banana', 'orange']
fruits.append('cherry')
print(fruits)

fruits.insert(2, 'kiwi')
print(fruits)

favorite_fruits = ['mango', 'lemon', 'pineapple']
fruits.extend(favorite_fruits)
print(fruits)

names = ['John', 'Eva', 'Laura', 'Nick', 'Jack']
names.remove('Laura')
print(names)
del names[1]
print(names)
del names[1:3]
print(names)
del names
# print(names) #should give error


# append(), extend(), insert(), remove(), del, len()
# list[start: stop: step]
# [expression for item in list if condition == True]

numbers = [1, 2, 3, 4]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers) # Output: [2, 4, 6, 8]

doubled_numbers = [num for num in doubled_numbers if num % 3 == 0]
print(doubled_numbers) # Output: [6]
print(doubled_numbers) # double is now changed

pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print(pairs)