# print('Hello World\nwelcome', 100)

# name = 'Derick'
# age = 28
# print(name + ' is a boy')
# print(name + ' is', age)
# print(name + ' is from Kenya')
# print(name.lower())
# print(name.upper())
# print(name.islower())
# print(name.replace('i','l'))
# print(min(3,5,7,89,-1))
# print(bin(4))
# name = input('Kindly type your name: ')
# age = int(input('Kindly type your age:'))
# print('Your name is ' + name + ' and you are ', age ,'years old')


# sentence = input('Enter your sentence:')
# print('Your typed as follows: '+sentence)
# word1 = input('Enter the word to replace: ')
# word2 = input('Enter the word to replace it with: ')
# print(sentence.replace(word1, word2))

# countries = ['Kenya', 'Germany', 'Egypt', 'Holland', 'USA', 'Qatar', 'Canada']
# print(countries)
# print(type(countries))
# countries[3] = 'Netherlands'
# print(countries)
# print(len(countries))

# countries = list(('Kenya', 28, True, 'Uganda'))
# print(countries)

# list1 = [1, 2, 3, 4, 5]
# list2 = ['banana', 'avocado', 'mango', 'oranges']
# list3 = list2.copy
# list1.pop()
# print(list1)
# list2.insert(1, 'tomato')
# print(list2)
# list2.remove('avocado')
# print(list2)
# print(list2.count('oranges'))
# list1.reverse()
# print(list1)
# print(list3)

# Tuples are like lists but they are immutable
# three_numbers = (2,19,3)
# print(three_numbers[1])
# names = ('Noun', 'tree', 'computer')
# print(names)
# print(type(three_numbers))

# functions is a type of code that perfoms a particular task and can be easily reused by calling it.
# def greetings_function(name, age):
#     print('Welcome ' + name + ' you are ', age, 'years old')

# greetings_function('Derick', 28)

# def greetings_function(name, age):
#     print('Welcome ' +name+ '. You are ', age, ' years old.')

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# greetings_function(name, age)

# use of return 
# def add_num(num1, num2):
#     return num1 + num2

# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# print(add_num(num1, num2))

# if statements in python
# a = 21
# b = 3*70

# if a == b:
#     print(str(a) + ' is equal to '+ str(b))

# elif a == False:
#     print('A is false')

# else:
#     print('A is none of the above')

# value = input('Enter your value here: ')

# if type(value) ==str:
#     print(value + ' is a string')
# elif type(value) == int:
#     print(value + ' is an integer.')
# elif type(value) == list:
#     print(value + ' is a list')
# else:
#     print('We don\'t know the data type of ' + value)

# value = int(input('Enter a number: '))

# if value % 5 == 0:
#     print(value, ' your number is divisble by 5')
# else:
#     print(value, ' your number is not divisble by 5')


# num = int(input('Enter a number:'))

# if num % 2 == 0:
#     print('Even number')

# else:
#     print('Odd number')


# Dickionaries in python
# my_dict ={
#     'name': 'Derick',
#     'nationality':'African',
#     'Qualification': 'University',
#     'age': 28,
#     'friends': ['Peter', 'Paul', 'Jay']

# }
# print(my_dict)

# While loops

# i = 1
# while i < 6 or i == 6:
#     print(i)
#     i+=1

# i = 5
# while i < 10 and i == 5:
#     print(i)
#     i+=1

# for loop
# my_list = ['an', 'en', 'io']

# for letter in my_list:
#     print(letter)
#     if letter == 'en':
#         break

# mydict = {
#     'name': 'Derick',
#     'age': 28
# }
# for initials in mydict:
#     print(initials)

# for x in range(6,20):
#     print(x)

# 2D list
# my_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]


# print(my_list[1][2])

# nested list
# my_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for lists in my_list:
#     for row in lists:
#         print(row)

# simple calculator
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
operator = input('Enter operator: ')

if operator == '+':
    print('The sum of your numbers is ',num1+num2)

elif operator == '-':
    print('The difference is ', num1-num2)

elif operator == '*':
    print('The product of numbers is ', num1*num2)

elif operator == '/':
    print('The division of your numbers is ', num1/num2)

else:
    print('Invalid operator. Try again.')