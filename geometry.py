"""
MAT 2170: Lab 2
This module allows various geometric shapes to be drawn.

Submitted by:
"""

import math


def drawSquare(myTurtle, sideLength):
    """
    Causes a turtle to draw a square of a specified size.

    After drawing the square, the turtle returns to its original position,
    facing in its original heading, as shown below. Note the relationship
    of the square to the turtle's initial position.

            >+-------+
             |       |
             |       |
             |       |
             +-------+

    Args:
        myTurtle: the turtle which is to do the drawing
        sideLength: the length of each side of the desired square

    Returns:
        None
    """

    for i in range(4):
        # Draw a side of the square
        myTurtle.forward(sideLength)

        # Turn to make a right angle, preparing for the next side
        myTurtle.right(90)


def drawRegularPolygon(turtle, n, r):
    """
    Draws a regular n-sided polygon of radius r.
    :param turtle: The turtle object.
    :param n: The number of sides.
    :param r: The radius of the polygon.
    :return: None.
    """
    # we just use a case of the below function where n == m
    drawPartialRegularPolygon(turtle, n, n, r)

def drawPartialRegularPolygon(turtle, n, m, r):
    """
    Draws a regular n-sided polygon of radius r.
    :param turtle: The turtle object.
    :param n: The number of sides.
    :param m: The number of sides to actually draw.
    :param r: The radius of the polygon.
    :return: None.
    """
    # calculate the length of one side
    side_length = 2 * r * math.sin( (2 * math.pi) / (2 * n) )
    # get the external angle of the polygon
    ext_angle = 360/n
    # store initial turtle details so we can return easily
    init_heading = turtle.heading()
    init_pos = turtle.pos()

    # DRAW
    # go to the first vertex
    turtle.up()
    turtle.forward(r)
    turtle.left( 90 + (ext_angle / 2))
    # loop through each side
    turtle.down()
    for side in range(m):
        turtle.forward(side_length)
        turtle.left(ext_angle)
    # go back to where we started
    turtle.up()
    turtle.goto(init_pos)
    turtle.setheading(init_heading)


def drawCircle(turtle, radius):
    """
    Draws an approximation of a circle using the above polygon function.
    :param turtle: The turtle object.
    :param radius: Radius of the circle
    :return: None.
    """
    # 150 sides is a decent enough approximation for most screen resolutions
    drawRegularPolygon(turtle, 150, radius)


def drawSemicircle(turtle, radius):
    """
    Draws an approximation of a semicircle using the above polygon function.
    :param turtle: The turtle object.
    :param radius: Radius of the semicircle
    :return: None.
    """
    # 150 sides is a decent enough approximation for most screen resolutions
    drawPartialRegularPolygon(turtle, 150, 75, radius)