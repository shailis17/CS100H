'''
Shaili Soni
CS100, H01
Nov 30 2020
HW #11
'''

class Dog: #problem 1
    #this class represents a dog with a name, breed, set of tricks
    species = 'Canis familiaris' #problem 5
    
    def __init__(self, dogName, dogBreed): #problem 1
        self.name = dogName
        self.breed = dogBreed
        self.tricks = [] #problem 2

    def teach(self, trick): #problem 3
        self.tricks.append(trick)
        print(self.name, " knows ", trick)

    def knows(self, trick): #problem 4
        if trick in self.tricks:
            print(self.name, " knows ", trick)
            return True
        else:
            print(self.name, " does not know ", trick)
            return False

    
