#Drawing with a "pen"

import turtle
import math

#Create turtle object
bob = turtle.Turtle()
bob.hideturtle()

print(bob)

def draw_square(my_turtle,side):
    for i in range(4):
        my_turtle.fd(side) #forward "side" pixels
        my_turtle.lt(90) #trun left 90 degrees

draw_square(bob,50)

bob.penup()
bob.fd(150)
bob.pendown()

draw_square(bob,100)

#---------------------------------------------------

def draw_polygon(my_turtle, sides, side_length):

    angle = 360.0/sides
    
    for i in range(sides):
        my_turtle.fd(side_length)
        my_turtle.lt(angle)

draw_polygon(bob, 3, 150)

draw_polygon(bob, 36, 15)

#-----------------------------------------------------

def draw_circle(my_turtle, radius):

    length=(2*math.pi*radius)/36

    draw_polygon(my_turtle, 36, length)

draw_circle(bob, 150)

