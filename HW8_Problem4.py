'''
Shaili Soni
CS100, H01
Oct 29, 2020
HW8, Problem 4
'''
import random

count = 1
num = random.randrange(0,51)

print("I'm thinking of a number in the range 0-50. You have five tries to guess it.")

while count < 6:
    guess = int(input("Guess #" + str(count) + ": "))
    if guess > num:
        count += 1
        print("Try again, your guess was too high...")
    elif guess < num:
        count += 1
        print("Try again, your guess was too low...")
    else:
        print("Yay! You guessed the right number!!!")
        break


if guess != num:
    print("You lost :( ")
    
