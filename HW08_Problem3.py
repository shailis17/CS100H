'''
Shaili Soni
CS100, H01
Oct 29, 2020
HW8, Problem 3
'''

def enterNewPassword():
    length = False
    dig = False
    while length == False or dig == False:
        password = input("Enter a password: ")
        if len(password) >= 8 and len(password) <= 15:
            length = True
        else:
            print("Check length")
            continue

        for i in range(10):
            if password.count(str(i)) > 0:
                dig = True
                print("Valid Password")
                break
        if dig == False:
            print("Password needs a digit")
            continue

enterNewPassword()

