"""
Shaili Soni
CS100, Section H01
October 5, 2020
HW #6
"""

#Question 1:
def hasFinalLetter(strList, Letters):
    hasLetter = []
    for word in range(len(strList)):
        for l in range(len(Letters)):
            if(strList[word][-1] == Letters[l]):
                hasLetter.append(strList[word])
    return hasLetter

#TESTS!!!
S1 = ["hello", "banana", "potato", "google", "IDLE"]
L1 = ["A", "y", "u"]
print(hasFinalLetter(S1, L1)) #empty list
S2 = ["stuff", "trash", "parachute", "coding", "SOS"]
L2 = ["f","e","E"]
print(hasFinalLetter(S2, L2)) #list of 2 words
S3 = ["halloween", "october", "fall", "chilly"] 
L3 = ["n","r","y"]
print(hasFinalLetter(S3, L3)) #list of 3 words

#Question 2:
def isDivisible(maxInt, twoInts):
    nums = []
    for x in range(1, maxInt):
        if x%twoInts[0] == 0 and x%twoInts[1] == 0:
            nums.append(x)
    return nums

M1= 32
T1 = (16, 5)
print(isDivisible(M1, T1)) #empty list
M2 = 22
T2 = (7,3)
print(isDivisible(M2, T2))
M3 = 100
T3 = (4, 5)
print(isDivisible(M3, T3))
        
