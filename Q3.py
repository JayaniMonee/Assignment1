# Write a python program that calculates the factorial of a given number.

def factorial(num):
    f = 1
    for i in range(1, num + 1 , 1) :
        f *= i
    print('Factorial : ', f)

num = int(input('Number : '))
factorial(num)