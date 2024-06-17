''' Write a python program that checks if two strings are anagrams of each other.'''

def bubble_sort(lst):
    length = len(lst)
    for i in range(length):
        for j in range((i + 1), length, 1):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst 

def anagram_check(string1, string2):
    if len(string1) != len(string2) :
        print('{} & {} are not anagrams'.format(string1, string2))
        return

    lst1 = list(string1)
    lst2 = list(string2)
    sort1 = bubble_sort(lst1)
    sort2 = bubble_sort(lst2)

    if sort1 == sort2:
        print('{} & {} are anagrams'.format(string1, string2))
    else:
        print('{} & {} are not anagrams'.format(string1, string2))

string1 = input('String 1: ')
string2 = input('String 2: ')
anagram_check(string1, string2)
