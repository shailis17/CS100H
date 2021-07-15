"""
Shaili Soni
CS100, Section H01
September 28, 2020
HW #4
"""
#Question 1
a = 3
b = 4
c = 5
if a < b:
    print("OK")
if c < b:
    print("OK")
if a + b == c:
    print("OK")
if a**2 + b**2 == c**2:
    print("OK")

#Question 2
print("")
if a < b:
    print("OK")
else:
    print("NOT OK")
if c < b:
    print("OK")
else:
    print("NOT OK")
if a + b == c:
    print("OK")
else:
    print("NOT OK")
if a**2 + b**2 == c**2:
    print("OK")
else:
    print("NOT OK")

#Question 3
print("")
import turtle
paper = turtle.Screen()
pen = turtle.Turtle()

color = input("What color? ")
width = int(input("What line width? "))
length = int(input("What line length? "))
shape = input("line, triangle, square? ")

pen.color(color)
pen.width(width)

if shape == "line":
    pen.fd(length)

if shape == "triangle":
    for i in range(3):
        pen.fd(length)
        pen.right(120)

if shape == "square":
    for i in range(4):
        pen.fd(length)
        pen.right(90)
