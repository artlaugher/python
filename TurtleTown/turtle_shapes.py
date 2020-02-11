# Author: Arthur Nez
# Date: 2/2020
# Description: turtle functions that draw fun stuff

import turtle


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
    turt.pu()
    turt.goto(0, 100)
    turt.pd()
    for s in range(0, sides):
        turt.forward(length)
        turt.rt(360/sides)


def circle(turt, radius):
    """
    draw a circle with a given radius
    :param turt:
    :param radius:
    :return:
    """
    circ = 2 * radius * 3.14159
    turt.pu()
    turt.goto(0, 100)
    turt.pd()
    for s in range(0, 720):
        turt.forward(circ/720)
        turt.rt(0.5)


def circles(turt, radius):
    """
    draw a fun recursive circle / cone shape
    :param turt:
    :param radius:
    :return:
    """
    circ = 2 * radius * 3.14159
    turt.pu()
    turt.goto(0, 100)
    turt.pd()
    for s in range(0, 720):
        turt.forward(circ/720)
        turt.rt(0.5)
    if radius > 5:
        circles(turt,radius - 5)


def arc(turt, radius, degrees):
    """
    draw an arc of radius and angle in degrees
    """
    circ = 2 * radius * 3.14159
    turt.pu()
    turt.goto(0, 100)
    turt.pd()
    for s in range(0, degrees*2):
        turt.forward(circ/720)
        turt.rt(0.5)


# tom = turtle.Turtle()

# arc(tom, 75, 45)

turtle.mainloop()