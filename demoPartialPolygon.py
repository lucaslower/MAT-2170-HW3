"""
Demonstration of the drawPartialRegularPolygon() function.
Submitted by: Lucas Lower
"""
import geometry as geo
import turtle

# init turtle
t = turtle.Turtle()
t.speed(10)

# draw the polygons
for num_sides in range(1, 13):
    radius = 380 - (30 * num_sides)
    geo.drawPartialRegularPolygon(t, 12, num_sides, radius)

# exit on click please and thanks
turtle.Screen().exitonclick()