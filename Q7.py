''' Write a python program that takes a string as input and returns its length.'''

def length_string(string):
    l = 0
    for i in range(len(string)) :
        l += 1
    print('Length of', string, ':', l)

string = input('String : ')
length_string(string)