''' Write a program that asks the user for their name and then prints a greeting message.'''

def greet(name):
    print('{} hello !'.format(name))

name = input('Your Name : ')
greet(name)