# Author: Arthur Nez
# Date: 2/2020
# Description: turtle functions that draw fun stuff

import turtle
import math


def draw_squares(jim, x_loc, y_loc, size):
    """
    recursive square drawing function with turtle
    :param jim: turtle
    :param x_loc: starting point x
    :param y_loc: starting point y
    :param size: length of side of square
    """
    jim.pu()
    jim.goto(x_loc,y_loc)
    jim.pd()
    for i in range(0, 4):
        jim.forward(size)
        jim.rt(90)

    if size > 1:
        draw_squares(jim, x_loc + 10, y_loc - 10, size - 5)


def polygon(turt, length, sides):
    """
    uses a turtle to draw a polygon with sides number of sides of length length
    :param turt:  turtle
    :param length: length of each side
    :param sides: sides of a polygon
    """
    polyline(turt, length, sides, 360)


def polyline(turt, length, sides, angle):
    """
    uses a turtle to draw a line of a given length with a given number of sides covering a given angle
    :param turt:  turtle
    :param length: length of each side
    :param sides: sides of a polygon
    """
    for s in range(0, sides):
        turt.forward(length/sides)
        turt.rt(angle/sides)


def left_polyline(turt, length, sides, angle):
    """
    uses a turtle to draw a line of a given length with a given number of sides covering a given angle
    :param turt:  turtle
    :param length: length of each side
    :param sides: sides of a polygon
    """
    for s in range(0, sides):
        turt.forward(length / sides)
        turt.lt(angle / sides)


def circle(turt, radius):
    """
    draw a circle with a given radius
    :param turt:
    :param radius:
    :return:
    """
    circ = 2 * radius * math.pi
    polygon(turt, circ/360, 360)



def circles(turt, radius):
    """
    draw a fun recursive circle / cone shape
    :param turt:
    :param radius:
    :return:
    """
    circ = 2 * radius * math.pi
    turt.pu()
    turt.goto(0, 100)
    turt.pd()
    polygon(turt, circ/360, 360)
    if radius > 5:
        circles(turt, radius - 5)


def arc(turt, radius, angle):
    """
    draw an arc of radius and angle in degrees
    """
    circ = 2 * radius * math.pi
    arc_length = circ / 360 * angle
    print(arc_length)
    polyline(turt, arc_length, angle, angle)


def turtleflower(simon, length):

    polyline(simon, 100, 100, 90)
    simon.rt(180)
    left_polyline(simon, 100, 100, 180)




tom = turtle.Turtle()

turtleflower(tom, 15)

# circle(tom,52)

#arc(tom, 50, 270)



turtle.mainloop()