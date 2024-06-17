''' Write a python program that checks if a substring is present in a given string.'''

def substring_check(string, substring):
    if substring in string:
        print('{} present in {}'.format(substring, string))
    else:
        print('{} not present in {}'.format(substring, string))

mainstr = input('String : ')
substr = input('Substring : ')
substring_check(mainstr, substr)
