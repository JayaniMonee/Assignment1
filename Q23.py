''' Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.'''

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print('{} Celsius = {} Fahrenheit'.format(celsius, fahrenheit))

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print('{} Fahrenheit = {} Celsius'.format(fahrenheit, celsius))

celsius = int(input('Temperature in Celsius : '))
fahrenheit = int(input('Temperature in Fahrenheit : '))
celsius_to_fahrenheit(celsius)
fahrenheit_to_celsius(fahrenheit)
