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
