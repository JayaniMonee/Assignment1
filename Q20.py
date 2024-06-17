''' Write a python program that takes a list of numbers and returns their sum.'''

def sum_elements(lst) :
    s = 0
    for i in lst :
        s += i
    print('Sum of Elements : ', s)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_elements(lst)