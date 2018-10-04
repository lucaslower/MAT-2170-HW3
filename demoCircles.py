"""
Demonstration of the drawCircle() and drawSemicircle() functions.
Submitted by: Lucas Lower
"""
import geometry as geo
import turtle

# init turtle
t = turtle.Turtle()
t.speed(10)

# draw a normal, complete circle
geo.drawCircle(t, 300)

# draw a semicircle inside the above circle
geo.drawSemicircle(t, 200)

# exit on click please and thanks
turtle.Screen().exitonclick()