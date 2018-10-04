"""
Demonstration of the drawHeart() function.
Submitted by: Lucas Lower
"""
import geometry as geo
import turtle

# init turtle
t = turtle.Turtle()
t.speed(10)

# draw an outline heart
geo.drawHeart(t, 200)

# draw a filled heart (and reset our position)
t.up()
t.goto(0,0)
t.setheading(0)
t.down()
geo.drawFilledHeart(t, 80, "red")

# hide the turtle
t.hideturtle()

# exit on click please and thanks
turtle.Screen().exitonclick()