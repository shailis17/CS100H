'''
Shaili Soni
CS100, H01
Oct 29, 2020
HW8, Problem 2
'''

def twoWordsV2(integer, firstLetter):
    word1 = ''
    word2 = ''
    lst = []

    run = True
    while run:
        word1 = input("Enter a " + str(integer) + "-letter word please: ")
        if len(word1) == integer:
            lst.append(word1)
            run = False

    run = True
    while run:
        word2 = input("Enter a word beginning with " + firstLetter + " please: ")
        if word2[0] == firstLetter.upper() or word2[0] == firstLetter.lower():
            lst.append(word2)
            run = False

    return lst

print(twoWordsV2(4, 'B')) 
