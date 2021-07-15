"""
Shaili Soni
CS 100 Section H01
September 17, 2020
HW 02
"""
#1
print("QUESTION 1")
grades = ['A', 'B', 'A', 'A', 'C', 'A', 'B', 'B', 'B', 'C']
frequency = [grades.count('A'), grades.count('B'), grades.count('C'), grades.count('D'), grades.count('F')]
print("Grades: ", grades, "\nFrequency: ", frequency)

#2
print("\nQUESTION 2")
dog_breeds = ["collie", "sheepdog", "Chow", "Chihuahua"]
print(dog_breeds)
herding_dogs = dog_breeds[:2]
print(herding_dogs)
tiny_dogs = [dog_breeds[2], dog_breeds[3]]
print(tiny_dogs)
print("Persian" in dog_breeds)
 
