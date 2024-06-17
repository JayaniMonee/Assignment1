''' Write a program that asks the user for their birth year and calculates their age.'''

def age_calculator(birth_year, current_year) :
    if birth_year > current_year :
        print('Invalid')
    else :
        age = current_year - birth_year
        print('Your age : ', age, 'years')

birth_year = int(input('Your Birth Year : '))
current_year = int(input('Current Year : '))
age_calculator(birth_year, current_year)