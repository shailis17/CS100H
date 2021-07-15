"""
Shaili Soni
CS100, H01
Nov 12 2020
HW10, Problem 2
"""

def initialLetters(wordList):
    wordsDict = {}
    for word in wordList:
        key = word[0]
        val = []
        for w in wordList:
            if w[0] == key and w not in val:
                val.append(w)
        wordsDict[key] = val
    return wordsDict

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetters(horton))

seuss = ['Today', 'you', 'are', 'you!', 'That', 'is', 'truer', 'than', 'true!', 'There', 'is', 'no', 'one', 'alive', 'who', 'is', 'you-er', 'than', 'you!']
print(initialLetters(seuss))

disney = ["It's", 'kind', 'of', 'fun', 'to', 'do', 'the', 'impossible']
print(initialLetters(disney))

