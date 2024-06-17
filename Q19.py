''' Write a python program that removes all punctuation from a given string.'''

def remove_punctuations(string):
    puctuations = '!,.?&;:_-\\\'"'
    s = ''
    for i in string:
        if i not in puctuations:
            s += i
    print(s)

string = input('String: ')
remove_punctuations(string)
