# print('Welcome, create your account now.')
# username = input('Enter username: ')
# password = input('Enter password: ')

# print('Your account has been created succeffuly.')
# print('Login now!')

# username2 = input('Enter username: ')
# password2 = input('Enter password: ')

# if username == username2 and password == password2:
#     print('Logged in successfully')
# else:
#     print('Invalid credentials')

print('Welcome, create your account here.')
Username = input('Enter your preferred username: ')
Password = input('Enter your preferred password: ')

print('Account created succeffully!')
print('Login now')

Username2 = input('Enter username created: ')
Password2 = input('Enter same password: ')

if Username == Username2 and Password == Password2:
    print('Logged in successfully!')
    print('Welcome to your account')
elif Username == Username2 and Password != Password2:
    print('Wrong password entered. Try again')
elif Username != Username2 and Password == Password2:
    print('Wrong username entered! Try again')

else:
    print('Wrong credentials found.')
    print('Create account first')
