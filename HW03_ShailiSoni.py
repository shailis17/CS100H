"""
Shaili Soni
CS100, Section H01
September 24, 2020
HW #3
"""
import turtle
pen = turtle.Turtle()

#inital position
pen.up()
pen.fd(-450)
pen.down()

#Number 1
side = 100

#Equilateral Triangle
pen.fd(side)
pen.left(120)
pen.fd(side)
pen.left(120)
pen.fd(side)
pen.left(120)

#move
pen.up()
pen.fd(side + 20)
pen.down()

#square
pen.fd(side)
pen.left(90)
pen.fd(side)
pen.left(90)
pen.fd(side)
pen.left(90)
pen.fd(side)
pen.left(90)

#move
pen.up()
pen.fd(side + 50)
pen.down()

#regular pentagon
pen.fd(side)
pen.left(72)
pen.fd(side)
pen.left(72)
pen.fd(side)
pen.left(72)
pen.fd(side)
pen.left(72)
pen.fd(side)
pen.left(72)


#Number 2
#adjust postion
pen.up()
pen.fd(400)
pen.down()

#circle 1
pen.circle(50)
#move
pen.up()
pen.right(90)
pen.fd(50)
pen.left(90)
pen.down()
#circle 2
pen.circle(100)
#move
pen.up()
pen.right(90)
pen.fd(50)
pen.left(90)
pen.down()
#circle 3
pen.circle(150)
#move
pen.up()
pen.right(90)
pen.fd(50)
pen.left(90)
pen.down()
#circle 4
pen.circle(200)

#Number 3:
import math
#a ==> 100!
a = math.factorial(100)
print("100! = ", a)
#b ==> the log (base 2) of 1,000,000
b = math.log(1000000,2)
print("the log (base 2) of 1,000,000 is: ", b)
#c ==> the greatest common divisor of 63 and 49
c = math.gcd(63,49)
print("the greatest common divisor of 63 and 49 is: ", c)


