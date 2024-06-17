# Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

def read_lines() :
    string = input('String : ')
    lines = ''
    while True :
        if string != '' :
            lines += string
            string = input('String : ')
        elif string == '' :
            print('Input Entered Successfully !')
            break
    print('\nInput {}'.format(lines))

read_lines()
