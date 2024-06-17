''' Write a python program that calculates the sum of the digits of a given number.'''

def sum_digits(number) :
    string = str(number)
    s = 0
    for i in string :
        s += int(i)
    print('Sum of Digits : {}'.format(s))

number = int(input('Number : '))
sum_digits(number)

