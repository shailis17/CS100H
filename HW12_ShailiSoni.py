'''
Shaili Soni
CS100, H01
Dec 10, 2020
HW #12
'''

#Problem 1
def safeOpen(filename):
    try:
        inF = open(filename)
        return inF
    except(FileNotFoundError):
        return None

#Problem 2
def safeFloat(x):
    try:
        f = float(x)
        return f
    except(ValueError):
        return 0.0

#Problem 3
def averageSpeed():
    tries = 0
    speedSum = 0
    numSpeeds = 0
    while tries < 2:
        name = input('Enter file name: ')
        inF = safeOpen(name)
        if inF == None:
            print('File Not Found. Try Again!')
            tries += 1
        else:
            break
    if tries == 2:
        return 'File Not Found. Goodbye!'
    else:
        import string
        for line in inF:
            speedList = line.split()
            for speed in speedList:
                if safeFloat(speed) > 2:
                    numSpeeds += 1
                    speedSum += safeFloat(speed)
    finalAvg = speedSum/numSpeeds
    return 'Average speed is ' + str(finalAvg) + ' miles per hour.'
