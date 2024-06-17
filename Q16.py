''' Write a program in python that counts the frequency of each character in a string.'''

def frequency_all_elements(lst):
    frequency_lst = []
    for i in lst:
        c = 0
        for j in lst:
            if i == j:
                c += 1
        frequency_lst.append(c)
    for i in range(len(lst)):
        print('Frequency of {} : {}'.format(lst[i], frequency_lst[i]))

lst = [1, 2, 3, 2, 3, 2, 2, 3, 4, 5, 5, 1]
frequency_all_elements(lst)

