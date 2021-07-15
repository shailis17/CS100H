"""
Shaili Soni
CS100, H01
Nov 5, 2020
HW9 Problem 1
"""

def file_copy(in_file, out_file):
    inFile = open(in_file)
    outFile = open(out_file, 'w')

    for line in inFile:
        outFile.write(line)

    inFile.close()
    outFile.close()

file_copy('created_equal.txt', 'copy.txt')


