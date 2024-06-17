''' Write a python program that concatenates two strings and returns the result.'''

def concatenate_string(string1, string2) :
    cString = string1 + string2
    print('Concatenated String :', cString)

string1 = input('String 1 : ')
string2 = input('String 2 : ')
concatenate_string(string1, string2)