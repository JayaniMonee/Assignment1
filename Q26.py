''' Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.'''

def prefix_sufix(prefix, string, sufix) :
    if prefix == string[ : len(prefix)] :
        print('{} starts with {}'.format(string, prefix))
    elif prefix != string[ : len(prefix)] :
        print('{} does not starts with {}'.format(string, prefix))

    if sufix == string[-len(sufix) : ]:
        print('{} ends with {}'.format(string, sufix))
    elif sufix != string[-len(sufix) : ]:
        print('{} does not ends with {}'.format(string, sufix))

string = 'daisy sugar plum'
prefix_sufix('plum', string, 'daisy')
        