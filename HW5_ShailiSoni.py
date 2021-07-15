"""
Shaili Soni
CS100, Section H01
October 1, 2020
HW #5
"""

#Question 1:
months = ["January","February","March","April","May","June","July",
          "August", "September", "October", "November", "December"]
for i in range(len(months)):
    if months[i][0] == "J":
        print(months[i])

#Question 2
print("")
for x in range(100):
    if x%2 == 0 and x%5 == 0: #check if divisible by both 2 and 5
        print(x)

#Question 3
print("")
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for h in range(len(horton)):
    for v in range(len(vowels)):
        if horton[h] == vowels[v]: 
            print(horton[h])



