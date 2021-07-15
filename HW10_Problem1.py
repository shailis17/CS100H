"""
Shaili Soni
CS100, H01
Nov 12 2020
HW10, Problem 1
"""

def initialLetterCount(wordList):
    firstLetters = {}
    for word in wordList:
        key = word[0]
        val = 0
        for w in wordList:
            if w[0] == key:
                val += 1
        firstLetters[key] = val
    return firstLetters

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))

seuss = ['Today', 'you', 'are', 'you!', 'That', 'is', 'truer', 'than', 'true!', 'There', 'is', 'no', 'one', 'alive', 'who', 'is', 'you-er', 'than', 'you!']
print(initialLetterCount(seuss))

disney = ["It's", 'kind', 'of', 'fun', 'to', 'do', 'the', 'impossible']
print(initialLetterCount(disney))
