"""
Shaili Soni
CS100, H01
Nov 5, 2020
HW9 Problem 2
"""

def file_stats(in_file):
    inFile = open(in_file, 'r')
    linesList = inFile.readlines()
    numLines = len(linesList)
    inFile.close()

    inFile = open(in_file, 'r')
    content = inFile.read()
    inFile.close()

    
    
    wordList = content.split()
    numWords = len(wordList)
    numChar = len(content)
    
    print("lines: ", numLines)
    print("words: ", numWords)
    print("characters: ", numChar)


file_stats('copy.txt')

