# try: 
#     x = int(input('Enter an integer: '))
#     print(x)

# except ValueError:
#     print('Value not an integer')

# else:
#     print('Nothing went wrong')

# finally:
#     print('try except finished')

# reading files
# coun_file = open('country.txt', 'r')
# for line in coun_file.readlines():
#     print(line)

# coun_file.close()


# writing files
# coun_file = open('counti.txt', 'w')
# coun_file.write('This is new country file')

# append files
# coun_file = open('country.txt', 'a')
# coun_file.write('\nEgypt')

# classes and objects
# class Myclass:
#     x = 5

# p1 = Myclass()
# print(p1.x)

# class Person:
#     pass
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# name = input('Enter your name: ')
# age = input('Enter your age: ')


# p1 = Person(name, age)
# print(p1.name)
# print(p1.age)

# Inheritance
class Student():
    name = 'Derick'
    age = 28
    gender = 'male'
