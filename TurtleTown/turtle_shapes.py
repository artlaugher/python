# Author: Arthur Nez
# Date: 2/2020
# Description: Recursive function that draws a bunch of squares with Turtle

import turtle

def draw_squares(jim, x_loc, y_loc, size, num):
    jim.pu()
    jim.goto(x_loc,y_loc)
    jim.pd()
    for i in range(0, 4):
        jim.forward(size)
        jim.rt(90)
    if num == 0:
        return

    if size > 1:
        draw_squares(jim, x_loc + 10, y_loc - 10, size - 5, num)

    else:
        print("finished!")
    if num >= 1:
        draw_squares(jim, x_loc * -1, y_loc * -1, size, num -1)


turts = turtle.Turtle()

draw_squares(turts, -250, 250, 50, 4)



turtle.mainloop()