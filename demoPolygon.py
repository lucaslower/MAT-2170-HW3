"""
Demonstration of the drawRegularPolygon() function.
Submitted by: Lucas Lower
"""
import geometry as geo
import turtle

# init turtle
t = turtle.Turtle()
t.speed(10)

# setup our circle to inscribe these polygons within
t.up()
t.goto(0, 350)
t.setheading(180)
t.down()
t.circle(350)
t.up()
t.goto(0,0)
t.down()

# draw the polygons
for num_sides in range(2, 6):
    geo.drawRegularPolygon(t, num_sides, 350)

# exit on click please and thanks
turtle.Screen().exitonclick()