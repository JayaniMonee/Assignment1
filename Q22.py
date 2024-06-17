''' Write a python program that returns the minimum and maximum values in a list of numbers.'''

''' Method 1 '''

def bubble_sort(lst):
    length = len(lst)
    for i in range(length):
        for j in range((i + 1), length, 1):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst 

def extremes(lst) :
    sortedLst = bubble_sort(lst)
    maxElement = sortedLst[0]
    minElement = sortedLst[-1]
    print('Maximum Element : {} \nMinimum Element : {}'.format(maxElement, minElement))

lst1 = [9, 1, 5, 8, 4, 2, 7]
extremes(lst1)

''' Method 2 '''

def min_max(lst) :
    minNumber = lst[0]
    maxNumber = lst[0]
    for i in lst :
        if minNumber > i :
            minNumber = i
        elif maxNumber < i :
            maxNumber = i
    print('Maximum Number : {} \nMinimum Numer : {}'.format(maxNumber, minNumber))

lst2 = [23, 45, 1, 67, 89, 2]
min_max(lst2)