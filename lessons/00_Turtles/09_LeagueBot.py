""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=6000, height=6000)
screen.bgcolor("white")

t = turtle.Turtle()

... # Your Code Here
# Change the Turtle Image



import turtle


def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()

t.shapesize(.5,.5)
set_turtle_image(t, 'leaguebot_bolt.gif')
t.pencolor("blue")
t.pendown()
t.speed(1)
for t in range(5):
    t.forward(10)
    t.left(75)

turtle.exitonclick()     




















