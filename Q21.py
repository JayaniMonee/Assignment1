''' Write a python program that counts the occurrences of a specific element in a list.'''

def frequency_element(lst, target) :
    frequency = 0
    for i in lst :
        if target == i :
            frequency += 1
    print('Frequency of {} : {}'.format(target, frequency))

lst = [1, 2, 2, 3, 4, 4, 2, 2, 5]
frequency_element(lst, 2)