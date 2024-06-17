''' Write a python program that checks whether a given number is even or odd'''

def check(num):
    if num % 2 == 0 :
        print('Even Number')
    else :
        print('Odd Number')

num = int(input('Number : '))
check(num)