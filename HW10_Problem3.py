"""
Shaili Soni
CS100, H01
Nov 12 2020
HW10, Problem 3
"""

def shareOneLetter(wordList):
    wordsDict = {}
    for word in wordList:
        val = []
        for letter in word:
            for w in wordList:
                if letter in w and w not in val:
                    val.append(w)
        wordsDict[word] = val
    return wordsDict

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(shareOneLetter(horton), '\n')

seuss = ['I', 'speak', 'for', 'the', 'trees,', 'for', 'the', 'trees', 'have', 'no', 'tongues.']
print(shareOneLetter(seuss), '\n')

disney = ["It's", 'kind', 'of', 'fun', 'to', 'do', 'the', 'impossible']
print(shareOneLetter(disney))

