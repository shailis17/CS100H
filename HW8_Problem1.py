"""
Shaili Soni
CS100, HO1
Oct 29, 2020
HW8, Problem 1
"""

def twoWords(integer, firstLetter):
    word1 = ''
    word2 = ' '
    lst = []
    while True:
        word1 = input("Enter a " + str(integer) + "-letter word please: ")
        if len(word1) == integer:
            lst.append(word1)
            break

    while True:
        word2 = input("Enter a word beginning with " + firstLetter + " please: ")
        if word2[0] == firstLetter.upper() or word2[0] == firstLetter.lower():
            lst.append(word2)
            break

    return lst

print(twoWords(4, 'B'))         
    
