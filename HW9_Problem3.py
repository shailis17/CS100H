"""
Shaili Soni
CS100, H01
Nov 5, 2020
HW9, Problem 3
"""

def repeat_words(in_file, out_file):
    inFile = open(in_file)
    outFile = open(out_file, 'w')
    rep = []
    for line in inFile:
        lowercaseLine = line.lower().split()
        for token in lowercaseLine:
            if lowercaseLine.count(token) > 1:
                if token not in rep:
                    rep.append(token)
                    outFile.write(token + " ")
        outFile.write("\n")

    inFile.close()
    outFile.close()

inF = 'catInTheHat.txt'
outF = 'catRepWords.txt'
repeat_words(inF, outF)

        
            
